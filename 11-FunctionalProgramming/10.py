dist = float(input("Enter distance in km: "))
hr = int(input("Enter number of travel hours: "))
minu = int(input("Enter number of travel minutes: "))

fun = lambda dist, hr, minu: round(dist/(hr + minu / 60), 2)

res = fun(dist, hr, minu)
print(f"Average speed: {res} km/h") 