import csv
import json

with open("products.csv", "r", encoding="utf-8") as file:
    header_line = file.readline().strip()
    header_fields = [field.strip() for field in header_line.split(',')]
    
    
    a = csv.DictReader(file, fieldnames=header_fields, delimiter=",")
    
    data_list = [row for row in a]



    with open("products.json", "w", encoding="utf-8") as jss:
        json.dump(data_list, jss, indent=2)    
    #print("CSV Header:", a.fieldnames)
    
    
    

for row in a:
    for key, val in row.items():
        print(f"{key}: {val}")
    print("-" * 20)
   
        
