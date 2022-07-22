def days_fn(days, units):
    if units == "hours":
        return f"{days} are {days*24} hours"
    elif units == "minutes":
        return f"{days} are {days*24*60} minutes"
    else:
        return "unsupported unit"
def check_cal(unit_dictionary):
    try:
        user_ip = int(unit_dictionary["days"])
        if user_ip > 0:
            result = days_fn(user_ip, unit_dictionary["unit"])
            print(result)
        elif user_ip == 0:
            print("you entered 0 ,plz enter integer")
        else:
            print("you entered -ve value ,no convertion")
    except ValueError:
        print("invalid number")
