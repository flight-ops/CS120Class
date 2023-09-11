hours_worked_list=["","","","",""]
hourly_pay_list=["","","","",""]
gross_pay_list = ["","","","",""]

flag = 0
while flag < 5:
    val_hourly_pay = float(input("Enter your pay rate"))
    hourly_pay_list[flag] = val_hourly_pay
    print(hourly_pay_list)
    val_hours_worked = float(input("Enter your hours worked"))
    hours_worked_list[flag] = val_hours_worked
    print(hours_worked_list)
    print(flag)
    flag+=1
    


for iterator in range(5):
    gross_pay_list[iterator] = hourly_pay_list[iterator] * hours_worked_list[iterator]
    print(gross_pay_list)