#create variable to store string to be operated on
operand_string = "abbccddeeee"

operand_list = list(operand_string)
print(operand_list)

#create variable to store final result

count_of_letter = operand_list.count()
print(count_of_letter)

#use a for loop 
for letter in operand_string:
    currentindex=0
    #insert number of a given letter in the correct index
    operand_list.insert(currentindex+1,str(count_of_letter))
    print(operand_list)
#end result should be "ab2c2d2e4" 