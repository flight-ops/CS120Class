import csv

with open('Classwork\Object Oriented\grosspay.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter = ',')
    print(reader)
    line_count = int(0) 
    print (line_count)
    
    for row in csv_file:
        if (line_count==0):
            print("hurray!")
            print(f'Column names are:{",".join(row)}')
            line_count += 1