#like question 2 part 2

#objective: determine whether a string is a palindrome or not

#variable naming convention: [input/output]_[data type]_[scope]_[container function abbreviation]

def string_to_list_conversion(input_string_local_stlc):
    #take argument and convert to list
    input_list_local_stlc = list(input_string_local_stlc)
    
    #create a copy of the original list to avoid pass-by-value stupidity
    reversed_list_local_stlc = input_list_local_stlc.copy()
    reversed_list_local_stlc.reverse()

    #return local lists to main function
    return input_list_local_stlc, reversed_list_local_stlc

#check for reciprocity, default condition is no
def check_lists_for_reciprocity(input_list_local_clfr,reversed_list_local_clfr):
    palindrome_true_false_local = False
    if input_list_local_clfr == reversed_list_local_clfr:
        palindrome_true_false_local = True
      
    else:
        palindrome_true_false_local = False

    return palindrome_true_false_local

def print_to_user(input_string_ptu, palindrome_true_false_ptu):
        if palindrome_true_false_ptu == True:
            print(input_string_ptu, "is a palindrome.")
        else:
            print(input_string_ptu, "is not a palindrome.")

def main():
    print("Palindrome Tester")
    input_string_main = input("What string would you like to test?")
    #obtain a list returned from the function 
    input_list_main, reverse_input_list_main = string_to_list_conversion(input_string_main)

    palindrome_true_false_main = check_lists_for_reciprocity(input_list_main,reverse_input_list_main)

    print_to_user(input_string_main,palindrome_true_false_main)


i = 10
while i == 10:
    main()