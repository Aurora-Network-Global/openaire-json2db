# Load libraries needed for running the script
import os
import gzip
import json
from pymongo import MongoClient
import yaml
from sys import exit

# Load configuration from config.yaml
try:
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
except FileNotFoundError:
    print("Error: 'config.yaml' file not found.")
    exit(1)
except yaml.YAMLError as e:
    print(f"Error parsing 'config.yaml': {e}")
    exit(1)
    
# MongoDB connection parameters
MONGO_URI = config['MONGO_URI']
DB_NAME = config['DB_NAME']
COLLECTION_NAME = config['COLLECTION_NAME']

# File parameters
SCHEMA_FILE = config['SCHEMA_FILE']
JSON_PARTS_DIR = config['JSON_PARTS_DIR']

def remove_definitions_from_schema(json_schema):
    """
    Remove the 'definitions' keyword and any references to it from the JSON schema.
    """
    if "definitions" in json_schema:
        del json_schema["definitions"]
    
    # Recursively remove from nested objects
    for key, value in list(json_schema.items()):  # Create a list of items for iteration
        if isinstance(value, dict):
            remove_definitions_from_schema(value)
            
    return json_schema

def remove_ref_from_schema(json_schema):
    """
    Remove the '$ref' keyword and any properties containing it from the JSON schema.
    """
    if "$ref" in json_schema:
        del json_schema["$ref"]
    
    # Recursively remove from nested objects and arrays
    keys_to_delete = []
    for key, value in json_schema.items():
        if isinstance(value, dict):
            if "$ref" in value:
                keys_to_delete.append(key)  # Mark the key for deletion
            else:
                remove_ref_from_schema(value)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    remove_ref_from_schema(item)
    
    # Delete marked keys
    for key in keys_to_delete:
        del json_schema[key]

    return json_schema

def replace_integer_with_long(json_schema):
    """
    Recursively replace the type 'integer' with 'long' in the JSON schema.
    """
    if isinstance(json_schema, dict):
        for key, value in json_schema.items():
            if key == "type" and value == "integer":
                json_schema[key] = "long"
            else:
                replace_integer_with_long(value)
    elif isinstance(json_schema, list):
        for item in json_schema:
            replace_integer_with_long(item)
    return json_schema


def convert_to_mongodb_schema(json_schema):
    # Handle unsupported keywords
    unsupported_keywords = ["$schema"]
    for keyword in unsupported_keywords:
        if keyword in json_schema:
            print(f"Warning: Removing unsupported keyword '{keyword}' for MongoDB validation.")
            del json_schema[keyword]

    # Remove 'definitions' keyword
    json_schema = remove_definitions_from_schema(json_schema)

    # Remove '$ref' keyword
    json_schema = remove_ref_from_schema(json_schema)
    
    # Replace 'integer' type with 'long'
    json_schema = replace_integer_with_long(json_schema)

    # Convert JSON schema to MongoDB format
    keyword_mapping = {
        "properties": "properties",
        "required": "required",
        "type": "bsonType"
    }
    mongodb_schema = {}
    for key, value in json_schema.items():
        if key in keyword_mapping:
            new_key = keyword_mapping[key]
            if isinstance(value, dict):
                mongodb_schema[new_key] = convert_to_mongodb_schema(value)
            else:
                mongodb_schema[new_key] = value
        else:
            mongodb_schema[key] = value

    return mongodb_schema

# Load the provided JSON schema 
try:
    with open(SCHEMA_FILE, "r") as file:
        original_schema = json.load(file)
except FileNotFoundError:
    print(f"Error: Schema file '{SCHEMA_FILE}' not found.")
    exit(1)
except json.JSONDecodeError as e:
    print(f"Error parsing JSON schema file: {e}")
    exit(1)

# Convert the provided JSON schema to MongoDB format
mongodb_schema = {
    "$jsonSchema": convert_to_mongodb_schema(original_schema)
}
print(json.dumps(mongodb_schema, indent=4))  # Pretty print the schema

VALIDATOR = {
    "$jsonSchema": mongodb_schema["$jsonSchema"]
}

# List all gzipped JSON files in the specified directory
json_files = [f for f in os.listdir(JSON_PARTS_DIR) if f.endswith(".json.gz")]

def load_data_to_mongodb_with_validation_updated():
    # Establish a connection to the MongoDB server
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    
    # Check if the collection already exists
    collection_names = db.list_collection_names()
    if COLLECTION_NAME in collection_names:
        # Update the validator for the existing collection
        db.command("collMod", COLLECTION_NAME, validator=VALIDATOR)
    else:
        # Create a new collection with the schema validator
        db.create_collection(COLLECTION_NAME, validator=VALIDATOR)
        
    collection = db[COLLECTION_NAME]
    
    # Loop through each gzipped JSON file in the directory
    for filename in json_files:
        filepath = os.path.join(JSON_PARTS_DIR, filename)
        try:
            with gzip.open(filepath, 'rt') as file:
                for line in file:
                    record = json.loads(line)
                    collection.insert_one(record)
        except FileNotFoundError:
            print(f"Error: File '{filepath}' not found.")
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON data from '{filepath}': {e}")
        except pymongo.errors.PyMongoError as e:
            print(f"Error inserting data into MongoDB: {e}")
    
    # Close the MongoDB connection
    client.close()

# Execute the function
load_data_to_mongodb_with_validation_updated()
