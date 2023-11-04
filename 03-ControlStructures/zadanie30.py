#funkcja aby przekonwertować 24 na 12
def convert_to_12_hour_format(time_24_hour):
    #split, rozdziel czas na godziny i minuty
    hours, minutes = map(int, time_24_hour.split(":"))
    
    #zadeklaruj czy jest am albo pm 
    period = "am" if hours < 12 else "pm"
    
    #przekonwertuj na format 12-godzinny
    if hours == 0:
        hours = 12
    elif hours > 12:
        hours -= 12
        
    time_12_hour = f"{hours:0d}:{minutes:02d}{period}"
    return time_12_hour

time_24_hour = input("Enter time (24-hour format): ")

time_12_hour = convert_to_12_hour_format(time_24_hour)
print("Time in 12-hour format:",time_12_hour)