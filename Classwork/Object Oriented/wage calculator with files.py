#objective: take in a file input with details like name, wage, hours worked
#read these values and generate values for grosspay
#append values to existing csv, or create a new file.

import csv

#open a file


with open('employee_details.csv') as csv_file:
    csv.reader = csv.reader(csv_file, delimiter = ',')
    line_count = 0
    for row in csv_file:
        if line_count ==0:
            print(f'Column names are:{",".join(row)}')
            line_count += 1
        print(f'\t{row["name"]} earns {row["hourly wage"]} per hour and worked for {row["hours worked"]}.')
        grosspay = (row[2] * row[3])
        print(f'They have earned ')
        line_count +=1
    print(f'Processed {line_count} lines.')
#store value in file


#finish file







total_employee_count = int(input("How many gross pay values do you need?"))


employee_name_list= ['' for i in range (total_employee_count)]
hours_worked_list=['' for i in range (total_employee_count)]
hourly_pay_list=['' for i in range (total_employee_count)]
gross_pay_list = ['' for i in range (total_employee_count)]

flag = 0
while flag < (total_employee_count):
    print("Employee" , str(flag+1))
    employee_name_list[flag] = input("What is your name?")
    print(employee_name_list)
    hourly_pay_list[flag] = float(input("Enter your pay rate"))
    print(hourly_pay_list)
    hours_worked_list[flag] = float(input("Enter your hours worked"))
    print(hours_worked_list)
    flag+=1
    
print("Okay, here is how much money everyone made.")
for iterator in range(total_employee_count):
    gross_pay_list[iterator] = hourly_pay_list[iterator] * hours_worked_list[iterator]
    print(employee_name_list[iterator])
    print(gross_pay_list[iterator])



