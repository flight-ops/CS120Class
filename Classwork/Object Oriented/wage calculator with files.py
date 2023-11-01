#objective: take in a file input with details like name, wage, hours worked
#read these values and generate values for grosspay
#append values to existing csv, or create a new file.
import csv

#open a file

class EmployerCalculator:

    def __init__(self):
        pass

    def file_loader():
        print("opening file")
        with open('Classwork\Object Oriented\grosspay.txt') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = ',')
            line_count = 0 
            
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are: {",".join(row)}')
                    line_count += 1
                else:
                    print("woohoo")
                # print(f'\t{row["name"]} earns {row["hourly wage"]} per hour and worked for {row["hours worked"]}.')
            #     grosspay = (row[2] * row[3])
            #     print(f'They have earned ')
            #     line_count +=1
            # print(f'Processed {line_count} lines.')
    # def file_writer():
    #         with open('Classwork\Object Oriented\grosspay.txt') as csv_file:
    #              csv_writer = csv.writer(csv_file,delimiter = ',')
    #              line_count = 0
    #              for row in csv_writer:
    #                 if line_count != 0:
    #                     csv_writer[4].write_row(row[2]*row[3])
                      
mycalc = EmployerCalculator

mycalc.file_loader

#store value in file


#finish file

