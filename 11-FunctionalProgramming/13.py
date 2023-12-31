def tolerance1(capacity, tolerance):
    def check_tolerance(filled_volume):
        lower_limit = (100 - tolerance) / 100 * capacity
        upper_limit = (100 + tolerance) / 100 + capacity
        return lower_limit <= filled_volume <= upper_limit
    return check_tolerance

def check_bottle_filling(bottle_capacity, filled_volume):
    if bottle_capacity == 500:
        tolerance = 2
    elif bottle_capacity == 1000:
        tolerance = 3
    elif bottle_capacity == 1500:
        tolerance = 5
    else:
        print("Invalid bottle capacity")
        return False
    
    check_function = tolerance1(bottle_capacity, tolerance)
    result = check_function(filled_volume)
    return result


print("507:", check_bottle_filling(500, 507))  # True
print("489:", check_bottle_filling(500, 489))  # False
print("984:", check_bottle_filling(1000, 984))  # True
print("1032:", check_bottle_filling(1000, 1032))  # False
print("1578:", check_bottle_filling(1500, 1578))  # False
print("1430:", check_bottle_filling(1500, 1430))  # True