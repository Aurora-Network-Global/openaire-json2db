# Load libraries needed for running the script
try:
    import os
    import gzip
    import json
    from pymongo import MongoClient
    import yaml
except ImportError as e:
    print(f"Error importing necessary modules: {e}")
    exit(1)

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

def convert_to_mongodb_schema(json_schema):
    """
    Convert JSON schema to a format suitable for MongoDB validation.
    This is a basic converter and may not handle all intricacies of the JSON schema.
    """
    # MongoDB uses a different set of keywords for schema validation
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

# Use the converted MongoDB schema to validate the ingested data
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
