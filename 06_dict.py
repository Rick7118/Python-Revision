#Dictionary

#Consists of key value pairs

student = {
    "name": "Subhayu",
    "age": 21,
    "skills": ["python","ai"]
}

#Accessing the values

print(student["name"])
print(student["age"])

#Updating the value

student["age"] = 22
student["skills"].append("backend")
student["city"] = "Kolkata"

#Removing

student.pop("age")
student.popitem()

#Checking if a key exists

"name" in student

#Looping through a dictionary

for key in student:
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(key, "=", value)


#Nested Dictionaries

person = {
    "name": "Rahul",
    "address": {
        "city": "Mumbai",
        "zip": 400001
    }
}

print(person["adress"]["city"])

#Dictionary Methods

# keys()        # all keys
# values()      # all values
# items()       # key-value pairs
# update()      # merge dictionaries
# clear()       # empty the dict
