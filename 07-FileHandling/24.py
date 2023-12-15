import csv

with open("fir.txt", newline='') as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)

    # Skip the header
    next(reader)

    # Print header 
    

    # Iterate through each row
    for row in reader:
        # Convert 'age' to an integer
        age = int(row[2])  # Assuming 'age' is the third column (index 2)

        # Check if the student is under 30
        if age < 30:
            # Print first name, last name, and email
            print(f"{row[0]}\t{row[1]}\t{row[4]}")  # Assuming 'first_name', 'last_name', and 'email' columns