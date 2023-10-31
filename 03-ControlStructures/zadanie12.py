name = input("Enter first person name: ")
age = int(input("Enter first person age: "))
name2 = input("Enter second person name: ")
age2 = int(input("Enter second person age: "))
if age >=18 and age2 >= 18:
    print(f"Both {name} and {name2} are adults")
elif age <= 18 and age2 >= 18:
    print(f"only {name2} is adult")
elif age >= 18 and age2 <= 18:
    print(f"only {name} is an adult")
else:
    print(f"Both of them are underage")