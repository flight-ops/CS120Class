# Objective: compress a string ex. abbccddeeee into something like "a1b2c2d2e4" with a letter and its counts

#main function
def main():
    #create variable to store string to be operated on, or maybe catch a user's input
    operand_string = input("What is the string you'd like to enter?")
    #convert to lowercase for convenience
    lowercase_converted_string = operand_string.lower()
    #operand_string = input("What is the string you'd like to compress?" (Only alphabet letters will appear in the result.))
    #create a list for all of the letters in the alphabet to check against
    alphabet_container_list = list("abcdefghijklmnopqrstuvwxyz")

    #convert the string provided either by default or by the user to a list or set
    operand_list = list(lowercase_converted_string)

    

    #print for debugging
    print("Original string:",operand_string)
    print("String in list form:",operand_list)
   
    #define a function to search for a letter
    def letter_searcher():
        #create a variable to store the output of the loop.
        output_string = ""
        #for each letter in the alphabet, check against a list that only contains alphabetical 
        for i in range (len(alphabet_container_list)):
            #check if the letter is found in the input string. If so,
            if operand_list.count(alphabet_container_list[i]) > 0:
                #set or reset the specific letter's count to zero
                specific_letter_count = 0
                #concatenate current letter being searched to output string
                output_string = output_string + (alphabet_container_list[i])
                #store value of the count of that letter in the input string
                specific_letter_count = operand_list.count(alphabet_container_list[i])
                #concatenate count of the letter (in string form) to the letter being counted
                output_string = output_string + str(specific_letter_count)
                print(output_string)
        return (output_string)
    

    #print a message for the user
    print("Compressing string...")
    #create a variable to store the value that letter_searcher() returns
    final_string = letter_searcher()
    #print the string so that the user can see it
    print("Compressed string:",final_string)

#call the function
main()

#result: desired result achieved, but really went way above and beyond (didn't really need the letters to be in order at all)
#reflection: was a good exercise in programming.