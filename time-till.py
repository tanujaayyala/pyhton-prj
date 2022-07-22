from datetime import datetime
user_ip = input("enter ur goal and date \n")
input_list = user_ip.split(":")
print(type(input_list))
goal = input_list[0]
dead_line = input_list[1]
dead_line_date = datetime.strptime(dead_line, "%d.%m.%Y")
time_today = datetime.today()
remaining = dead_line_date - time_today
print(f"dear user! you have {remaining} hours to {goal}")

