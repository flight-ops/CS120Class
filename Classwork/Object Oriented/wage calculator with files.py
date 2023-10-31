#objective: take in a file input with details like name, wage, hours worked
#read these values and generate values for grosspay
#append values to existing csv, or create a new file.
import csv

#open a file

class EmployerCalculator:

    def __init__(self):
        pass

    def file_loader():
        with open('Classwork\Object Oriented\grosspay.csv') as csv_file:
            reader = csv.reader(csv_file, delimiter = ',')
            print(reader)
            line_count = 0 
            for row in csv_file:
                if line_count ==0:
                    print(f'Column names are:{",".join(row)}')
                    line_count += 1


                # print(f'\t{row["name"]} earns {row["hourly wage"]} per hour and worked for {row["hours worked"]}.')
            #     grosspay = (row[2] * row[3])
            #     print(f'They have earned ')
            #     line_count +=1
            # print(f'Processed {line_count} lines.')

mycalc = EmployerCalculator

mycalc.file_loader()

#store value in file


#finish file

