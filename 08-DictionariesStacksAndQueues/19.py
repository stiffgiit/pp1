import json


with open("studentss.json", "r", encoding="utf-8") as orifile:
    oridata = json.load(orifile)
    
    
    
selected_keyz = [
    {
        "name": student['name'].split()[0], 
        "last_name": student['surname'],
        "student_id": student['student_ID']
        }
        for student in oridata
    ]


with open("idk.txt", "w") as file:
    json.dump(selected_keyz, file, indent=2)
    
    
    