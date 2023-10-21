#determine whether one string is one edit away from becoming another

#check which string is longer and determine which string should be the "complete" string
#logically, the incomplete string will be whichever one is shorter (since an incomplete string must be shorter than the complete string)

#if their lengths are equal, then they are definitely not one edit away
#else, return an error
def check_length(first_list_cl, second_list_cl):
#if the first string is longer, deem it the "complete" one
     if len(first_list_cl) > len(second_list_cl):
          return first_list_cl, second_list_cl
     
    #otherwise if the second string is longer, deem it the "complete" one
     elif len(first_list_cl) < len(second_list_cl):
          return second_list_cl, first_list_cl

#convert the strings to lists so that iteration methods can be used
def convert_strings_to_lists(complete_string_cstl, incomplete_string_cstl):
    complete_list_cstl = list(complete_string_cstl)
    incomplete_list_cstl = list(incomplete_string_cstl)
    return complete_list_cstl, incomplete_list_cstl

#the program creates possible variations by removing letters
#it does not add letters, which would create an unnecessarily large amount of variations
def generate_variations(complete_list_gv):
    #create a list to store possible incomplete variations
    incomplete_variations_gv = []

    for i in range(len(complete_list_gv)):
        #copy the original complete list
        new_list_gv = complete_list_gv.copy()
        #remove the letter at the specified index
        new_list_gv.pop(i)
        #append the iteration to the complete set of iterations
        incomplete_variations_gv.append(new_list_gv)
    return (incomplete_variations_gv)

#check if any variation of the complete string matches the incomplete string
def check_variations(incomplete_list_cv, possible_incomplete_lists_cv):
    one_edit_condition = False
    if incomplete_list_cv in possible_incomplete_lists_cv:
        print("\nFound a match!")
        one_edit_condition = True
    else:
        print("\nDid not find a match.")
    return one_edit_condition

#check possible iterations of strings that are one edit away.
#if one is found, break the loop and tell the user
#if not, tell the user that something is false

def output_results(one_edit_condition_or,first_string_or,second_string_or):
    if one_edit_condition_or == True:
        print("\nTrue:",first_string_or,"is one edit away from being",second_string_or+".")
    elif one_edit_condition_or == False:
        print("\nFalse:",first_string_or,"is not one edit away from being",second_string_or+".")

def main():
    first_string_main = input("What is the first string you'd like to check? ")
    second_string_main = input("What is the string you'd like to check? ")
    
    first_list_main, second_list_main = convert_strings_to_lists(first_string_main, second_string_main)

    complete_list_main, incomplete_list_main = check_length(first_list_main, second_list_main)

    incomplete_variations_main = generate_variations(complete_list_main)
    
    one_edit_condition_main = check_variations(incomplete_list_main, incomplete_variations_main)

    output_results(one_edit_condition_main,first_string_main,second_string_main)

flag = 0
while flag == 0:
    main()
    continue_condition = input("\nWant to continue? y/n\t")
    if continue_condition == "y":
        print("Cool, continuing.")
        continue
    elif continue_condition == "n":
        print("Have a nice day.")
        break
