def month(n):
    month_name = ["January", "February", "March",
                  "April", "May", "June", "July",
                  "August", "September", "Novebemer", "October",
                  "December"]
    return month_name[n-1]

month_to_display = [1, 9, 12]

for month_number in month_to_display:
    print(f"Month number: {month_number}")
    print(f"Month name: {month(month_number)}")
    print()
