winter_semester = {
    "math": 60,
    "programming": 30,
    "history": 15
}

lis = []

for val in winter_semester.values():
    lis.append(val)
a = sum(lis)
print("Total number of hours in the winter semester is ",a)