#main function
def main():
    #create variable to store string to be operated on, or maybe catch a user's input
    operand_string = "abbccddeeee"
    #create a list for all of the letters in the alphabet
    alphabet_container_list = list("abcdefghijklmnopqrstuvwxyz")

    #convert the string provided either by default or by the user to a list or set
    operand_list = list(operand_string)

    #create a variable to store the output of the loop.
    output_string = ""

    #print for debugging
    print(operand_string)
    print(operand_list)
   


    #for each letter in the alphabet, 
    for i in range (len(alphabet_container_list)):
        #check if the letter is found in the input string. If so,
        if operand_list.count(alphabet_container_list[i]) > 0:
            #set a variable to zero
            specific_letter_count = 0
            #concatenate current letter to output string
            output_string = output_string + (alphabet_container_list[i])
            #store value of the count of that letter in the input string
            specific_letter_count = operand_list.count(alphabet_container_list[i])
            #concatenate count of the letter (in string form) to the letter being counted
            output_string = output_string + str(specific_letter_count)

    print (output_string)


main()