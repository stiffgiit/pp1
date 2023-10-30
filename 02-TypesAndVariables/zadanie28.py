height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
bmi = round(weight/(height/100)**2)
print("Your BMI index: ",bmi)
if bmi >= 18.5 and bmi <= 24.9:
    print("Correct weight: True")
else:
    print("Correct weight: False")    