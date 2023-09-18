#prompt user for input in kilometers


i = 1


def calculate_conversion():
    miles_output= ''
    kilometers_input = float(input("What is the # of km you want to convert to mi?"))
    miles_output = kilometers_input * 0.6214
    print (str(kilometers_input),"km is equal to",str(round(miles_output,7)),"mi")

while i == 1:
    calculate_conversion()