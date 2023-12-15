countries = [
    {"name": "Poland", "population": 3800000},
    {"name": "Yemen", "population": 50200000},
    {"name": "Niger", "population": 7800000},
    {"name": "USA", "population": 32100000},
    {"name": "Lithuania", "population": 800000},
]

print("COUNTRY\tPOPULATION")

count = 0


while count < len(countries):
    key = countries[count]
    val = key["name"]
    pp = key["population"]
    print(f"{val}\t{pp}")
    count += 1
    
    
