import random

def create_list():
    local_list = []
    #generate a list of random length (min. 1 value) and append random values each time.
    for i in range (random.randint(1,20)):
        local_list.append(random.randint(0,10))
    #print original list for debug
    print ("The locally generated list is:", local_list)
    print ("There are", len(local_list),"values in the list.")
    print ("Please choose an index between 0 and",len(local_list)-1,"to leave out.")
    #return local list to main function to create main_list
    return local_list


def print_except_given_argument(main_list, excepted_index):
    print("Changing list...")
    print("The excepted index is:", excepted_index)
    print("The old list is", main_list)
    del main_list[excepted_index]
    new_main_list = main_list
    return new_main_list

    #print original list
    #print ("The original list is:", main_list)
    #invoke other functions, print new function at the end
def main():
    main_list = []
    main_list = create_list()

    excepted_index = int(input("What index would you like to leave out?"))

                 
    #invocation provides main_list values to the function      
    print("The new list is", print_except_given_argument(main_list, excepted_index))

#invoke main
main()