grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2.0]

program = list(filter(lambda grade: grade != 2.0, grades))
average_grade = sum(program) / len(program) if len(program) > 0 else 0.0

print(f"Arithmetic mean for grades <> 2.0 is {average_grade:.2f}")