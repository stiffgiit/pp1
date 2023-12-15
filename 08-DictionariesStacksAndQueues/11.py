import json

movie = {
    "title": "Destruction",
    "year": 2015,
    "actor": {"leading": "Jake Gyllenhaal", "supporting": "some d class actors"},
    "oscar": False,
    "grade": "cool"
}

a = json.dumps(movie, indent=4)

with open("fav.json", "w") as file:
    file.write(a)
