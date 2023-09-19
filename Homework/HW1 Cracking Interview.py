#create variable to store string to be operated on, or maybe catch a user's input
operand_string = "abbccddeeee"
#create a list for all of the letters in the alphabet
alphabet_container_list = list("abcdefghijklmnopqrstuvwxyz")

#print for debugging, remove later
#print(alphabet_container_list)

#convert the string provided either by default or by the user to a list that can be read one by one
operand_list = list(operand_string)

#print for debugging
#print(operand_list)

#create variable to store final result (or for functions to append to it midway)
output_string = ""


#function purpose: if the count is greater than 0, append the letter and the number of times it appears to the output string
def count_a_letter(current_letter_of_the_alphabet):
    #for each letter in the alphabet, check to see if the letter is in the operand string
    #if it is, append the letter and the number to the output string
    if operand_list.count(current_letter_of_the_alphabet) > 0:
        #print for debugging
        print(operand_list.count(current_letter_of_the_alphabet))



for i in range (len(operand_list)):
    specific_letter_count = count_a_letter((operand_list[i]))
    