import json

student = {
    "name": "Margot",
    "surname": "Robbie",
    "uni": "MIT",
    "year": 2,
    "major": "civil engineering"
}

with open("student.json", "w") as file:
    file.load(student)
    
a = json.dumps(student, indent=4)
print(a)