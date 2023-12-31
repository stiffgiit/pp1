def avg_speed(distance, hours, minutes):
    total_hours = hours + minutes / 60
    speed = round((distance/total_hours), 2)
    return speed


dist = float(input("Enter distance in km: "))
hour = int(input("Enter number of travel hours: "))
minu = int(input("Enter number of travel minutes: "))

avg = avg_speed(dist, hour, minu)

print(f"Average speed: {avg} km/h")