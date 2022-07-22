from demo import check_cal
usr_ip = ""
while usr_ip != "exit":
    usr_ip = input("enter a number and convertion unit seperated with coln:\n")
    days_unit = usr_ip.split(":")
    print(days_unit)
    unit_dictionary = {"days": days_unit[0], "unit": days_unit[1]}
    print(type(unit_dictionary))
    check_cal(unit_dictionary)