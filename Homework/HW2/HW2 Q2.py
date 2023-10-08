#function determines whether one string is a rotation of the other
#variable naming convention: [input/output]_[data type]_[scope]_[container function]

def reverse_checking_string(original_string,checking_string):
    #typecast strings to lists to make use of the 'reverse' method
    original_string_to_list = list(original_string)
    checking_string_to_list = list(checking_string)

    #if the second string IS a rotation of the first, then reversing the second string SHOULD make it equal to the first string
    #reverse the list form of the second string to check against the list form of the original string
    checking_string_to_list.reverse()

   #store list in a variable
    reversed_checking_list = checking_string_to_list
    
    #return the two lists to pass onto next function
    return original_string_to_list, reversed_checking_list

#check if the two lists are identical, return boolean to provide as argument to next function

def reverse_condition_checker(original_list, checking_list):
    if original_list == checking_list:
        reverse_true_condition_local = True
    else:
        reverse_true_condition_local = False

        #return boolean condition
    return reverse_true_condition_local

#depending on boolean condition, report a certain condition to the user
def print_output(original_string_local, string_for_checking_local, reverse_true_condition_local):
    if reverse_true_condition_local == True:
        print("True,",string_for_checking_local,"is a rotation of", original_string_local)
    else:
        print("False,",string_for_checking_local,"is not a rotation of", original_string_local)
    return


def main():
    #prompt user input, store
    original_string_input = input("What is your original string?")
    string_for_checking_input =input("What string would you like to check?")
    #feed user inputs to reverse_checking_string to obtain the two strings in list form
    original_list_main, reversed_checking_list_main = reverse_checking_string(original_string_input,string_for_checking_input)

    #check the original string and the now-reversed rotation string, get a boolean for whether or not the strings are rotated or not
    reverse_true_condition_main = reverse_condition_checker(original_list_main,reversed_checking_list_main)
    #print appropriate output given the boolean condition describing whether or not the strings are rotated versions of each other.
    print_output(original_string_input,string_for_checking_input,reverse_true_condition_main)

#call main
main()