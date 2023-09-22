# MongoDB Data Loader for OpenAIRE Community Data Dump

## Overview

This script, `create_tables_from_jsonschema.py`, is designed to load data from gzipped JSON files into a MongoDB collection, while also validating the data against a specified JSON schema.

## Purpose

The primary objectives of the script are:

1. **Configurable Database and File Parameters**: The script reads parameters such as MongoDB URI, database name, collection name, schema file, and directory containing gzipped JSON files from a configuration file (`config.yaml`).
  
2. **Schema Validation**: Before loading the data, the script converts the provided JSON schema to a MongoDB validation schema. This ensures that all data inserted into the MongoDB collection adheres to the defined schema.

3. **Dynamic File Loading**: Instead of working on a pre-defined set of filenames, the script dynamically reads and processes all gzipped JSON files present in the specified directory. This ensures flexibility and scalability for different data sets.

4. **Error Handling**: The script is equipped with comprehensive error handling mechanisms. It gracefully manages issues such as missing configuration files, invalid JSON schemas, data insertion errors, and more.

## Specific Use Case: Analysis of Dutch Research Output from OpenAIRE

The script has been utilized to process and analyze the data dump from OpenAIRE Community, specifically focusing on the Dutch Research Output. OpenAIRE provides comprehensive research data, and by extracting the Dutch-specific research output, the goal is to gain insights into the research trends, patterns, and contributions of Dutch academia.

By loading this data into a noSQL database (MongoDB in this case), we facilitate:
- **Dynamic Dashboards**: Interactive dashboards can be created to provide real-time insights into the research data, allowing for drill-down capabilities into specific research areas, institutions, or time frames.
  
- **Custom Reports**: With the data in MongoDB, custom reports can be generated to highlight specific trends, notable research contributions, or any other aspect of interest.

- **Data Analysis**: The structured storage in MongoDB aids in complex data analysis processes, from basic statistical analysis to machine learning models, to derive meaningful conclusions from the data.

## Usage

To run the script:

```bash
python create_tables_from_jsonschema.py
```

Make sure you have all the necessary Python packages installed and the `config.yaml` file properly set up before executing the script.

To do so follow the setup instructions below.


# Setup Instructions for OpenAIRE Data Loader

## 1. Installing Windows Subsystem for Linux (WSL)

1. Open PowerShell as Administrator and run the following command:
   
   ```bash
   wsl --install
   ```

2. Once installed, open the Microsoft Store, search for "Ubuntu", and install it.

3. Launch Ubuntu. The first time you launch it, you'll be prompted to create a user and set a password.

## 2. Installing Python

1. Update package lists and install prerequisites:
   
   ```bash
   sudo apt update
   sudo apt install software-properties-common
   ```

2. Add the deadsnakes PPA (Personal Package Archive) to your sources:

   ```bash
   sudo add-apt-repository ppa:deadsnakes/ppa
   ```

3. Install Python:

   ```bash
   sudo apt install python3.9
   ```

## 3. Installing Git

1. Install Git:

   ```bash
   sudo apt install git
   ```

2. (Optional) Configure Git:

   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "youremail@example.com"
   ```

## 4. Installing Docker

1. Update package lists:

   ```bash
   sudo apt update
   ```

2. Install Docker dependencies:

   ```bash
   sudo apt install apt-transport-https ca-certificates curl software-properties-common
   ```

3. Add Docker’s official GPG key:

   ```bash
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
   ```

4. Add Docker repository:

   ```bash
   sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
   ```

5. Install Docker:

   ```bash
   sudo apt update
   sudo apt install docker-ce
   ```

6. Start Docker:

   ```bash
   sudo systemctl start docker
   ```

7. Enable Docker to start on boot:

   ```bash
   sudo systemctl enable docker
   ```

## 5. Installing MongoDB using Docker

1. Pull the MongoDB Docker Image:

   ```bash
   docker pull mongodb/mongodb-community-server:latest
   ```

2. Run MongoDB as a Docker container:

   ```bash
   docker run --name mongo -d -p 27017:27017 mongodb/mongodb-community-server:latest
   ```

## 6. Cloning the Repository

1. Navigate to your desired directory and clone the repo:

   ```bash
   git clone https://github.com/ubvu/openaire-json2db.git
   ```

2. Navigate into the cloned directory:

   ```bash
   cd openaire-json2db
   ```

## 7. Setting Up Python Environment

1. Install `pip` and `virtualenv`:

   ```bash
   sudo apt install python3-pip
   pip3 install virtualenv
   ```

2. Create a new virtual environment:

   ```bash
   virtualenv venv
   ```

3. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

4. Install necessary Python packages:

   ```bash
   pip install -r requirements.txt
   ```

---

**Note**: Make sure you deactivate the virtual environment once you're done by running `deactivate`. 

This setup guide should provide a comprehensive walkthrough to get your environment up and running. Remember to back up any important data before making significant changes to your system, and always ensure that you have proper permissions for installations.