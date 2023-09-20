'''

JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy 
for humans to read and write and easy for machines to parse and generate. 
In Python, you can work with JSON data using the built-in json module, which provides 
functions for encoding and decoding JSON data.

'''
# Using json in python is dictated under json package
import json

# Python to JSON {Serialization | Encoding}

listi = ["name", "value", "description", "identity"]  # Python list

listi_To_json = json.dumps(listi)  # json method for converting listi to json

print(listi_To_json)

dicti = {
    "name": "dictionary",
    "type": "old school",
    "language": "Swahili",
}

dicti_To_json = json.dumps(dicti)

print(dicti_To_json)


# JSON to Python conversion {Deserialization | Decoding}

# JSON object
json_string = '{"name" : "John", "age" : 17, "gender" : "Male", "City" : "Amsterdam"}'

json_string_to_python = json.loads(json_string)  # Python object

print(json_string_to_python)


# Writing to a json file

data = {
    "name": "John",
    "age": 17,
    "city": "Carlifonia",
    "country": {
        "1st": "Netherlands",
        "2nd": "Tanzania",
    },
    "hobby": "Football",
    "wife": {

        "name": "Alice",
        "age": 28,
        "city": "Los Angeles",
        "email": "alice@example.com",
        "is_student": "true",
        "hobbies": ["reading", "painting", "traveling"],
        "address": {
                "street": "123 Main Street",
                "city": "Los Angeles",
                "zip_code": "90001"
        }
    }
}

with open("data.json", "w") as file:
    json.dump(data, file)


# Reading from a json file
with open("data.json", "r") as file:
    data = json.load(file)
print(data)
