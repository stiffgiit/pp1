x = round(float(input("x = ")))
y = round(float(input("y = ")))

if x == 0 and y == 0:
    position = "origin"
elif x == 0:
    position = "y-axis"
elif y == 0:
    position = "x-axis"
elif x > 0 and y > 0:
    position = "first quadrant"
elif x < 0 and y > 0:
    position = "second quadrant"
elif x < 0 and y < 0:
    position = "third quadrant"
else:
    position = "fourth quadrant"
    
print(f"Point P({x},{y}) is in the {position} of the coordinate system")