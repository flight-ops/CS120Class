#determine whether one string is one edit away from becoming another

#planning to reuse the code from q1, specifically the index exception code
def convert_strings_to_lists(complete_string_cstl, incomplete_string_cstl):
    complete_list_local_cstl = list(complete_string_cstl)
    incomplete_list_local_cstl = list(incomplete_string_cstl)

    return complete_list_local_cstl, incomplete_list_local_cstl

def create_variations(complete_list_local_crv):
    for i in range (len(complete_list_local_crv)-1):
        incomplete_list_iterator_local_crv = list(complete_list_local_crv).copy
        incomplete_list_iterator_local_crv.remove(i)
        print(incomplete_list_iterator_local_crv)


        list_of_possible_incomplete_lists_local_crv =[]
        list_of_possible_incomplete_lists_local_crv.append(incomplete_list_iterator_local_crv)

    return list_of_possible_incomplete_lists_local_crv


def check_variations(complete_list_local_cv, list_of_possible_incomplete_lists_local_cv):
    for i in range (len(complete_list_local_cv)-1):
        if complete_list_local_cv == list_of_possible_incomplete_lists_local_cv[i]:
            print("Found a match!")
            break
        else:
            print("Did not find a match.")
        


#check possible iterations of strings that are one edit away.
#if one is found, break the loop and tell the user
#if not, tell the user that something is false


#determine which string is longer, to determine order of

def main():
    complete_string_main = input("What is the complete string?")
    incomplete_string_main = input("What is the string you'd like to check?")
    complete_list_main, incomplete_list_main = convert_strings_to_lists(complete_string_main, incomplete_string_main)
    list_of_possible_incomplete_lists_main = create_variations(complete_list_main)

    check_variations(complete_list_main, list_of_possible_incomplete_lists_main)


main()
