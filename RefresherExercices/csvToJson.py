"""
CSV and JSON Libraries Overview

CSV (Comma-Separated Values):
    - CSV is a plain text format for storing tabular data (rows and columns)
    - Each line represents a row, with values separated by commas
    - Used for: data export/import, spreadsheets, data analysis, storing structured data
    
    Most Used Methods:
    - csv.reader() : Reads CSV files and returns an iterator of rows
    - csv.DictReader() : Reads CSV and returns dictionaries with headers as keys
    - csv.writer() : Writes data to CSV format
    - csv.DictWriter() : Writes dictionaries to CSV format

JSON (JavaScript Object Notation):
    - JSON is a lightweight, text-based data format for structured data
    - Uses key-value pairs, arrays, objects; language-independent
    - Used for: APIs, data interchange, configuration files, web applications, NoSQL databases
    
    Most Used Methods:
    - json.load() : Reads JSON from a file object, returns Python object (dict/list)
    - json.loads() : Parses JSON string, returns Python object (dict/list)
    - json.dump() : Writes Python object as JSON to a file object
    - json.dumps() : Converts Python object to JSON string
    
    Python to JSON Conversion:
    - Python dict → JSON object
    - Python list → JSON array
    - Python str → JSON string
    - Python int/float → JSON number
    - Python True/False/None → JSON true/false/null
    
    JSON to Python Conversion:
    - JSON object → Python dict
    - JSON array → Python list
    - JSON string → Python str
    - JSON number → Python int/float
    - JSON true/false/null → Python True/False/None
    
    Examples:
    - json.dumps({"name": "John", "age": 30}) → '{"name": "John", "age": 30}'
    - json.loads('{"name": "John", "age": 30}') → {"name": "John", "age": 30}
"""

import csv
import json

def cvs_json(file_name):
    #read the cvs file, convert it to a list of dictionaries
    with open(f"{file_name}.csv", "r") as csvFile :
        reader = csv.DictReader(csvFile)
        data = list(reader)
        for dic in data:
            if not dic.get("email") :
                dic["email"] = "N/A"

    #create a json file
    with open(f"{file_name}.json", "w") as jsonFile :
            json.dump(data, jsonFile, indent=4)



if __name__ == "__main__" :
    cvs_json("data")

    print("reading json")
    with open("data.json", "r") as jsonFile:
        print(jsonFile.read())

    print("Converting Json File into python obj")
    with open("data.json", "r") as jsonFile:
        python_obj = json.load(jsonFile)
        print(python_obj)
        #list of dictionaries
        print(type(python_obj))

