import random
#create a function to load a list
def create_list():
    local_list = []
    #generate a list of random length (min. 1 value) and append random values each time.
    for i in range (random.randint(1,20)):
        local_list.append(random.randint(0,10))
    #print original list for debug
    print ("The locally generated list is:", local_list)
    #return local list to main function to create main_list
    return local_list

#create a function to print all values in the list,
#except at the index passed in an argument

#take in main_list as an argument, as well as the index to be excepted.
def print_except_given_argument(main_list, excepted_index):
    print("Changing list...")
    print("The excepted index is:", excepted_index)
    #new local list to store values (except the one specified)
    new_local_list = []
    #for loop to iterate main_list
    for entry in range(len(main_list)):
        #check if index is excepted, if not, append to new list, if so, print a message for the user. 
        if entry != excepted_index:
            new_local_list.append(main_list[entry])

        #if the value is excepted, print a message to the user.
        elif entry == excepted_index:
            print ("excluding", main_list[entry],"at index", entry)
#return new_local_list to the function call inside of the print function, returns 
    return new_local_list
        

def main():
    main_list = []
    main_list = create_list()
    #print original list
    print ("The original list is:", main_list)
    #invoke other functions, print new function at the end
                  #invocation provides main_list values to the function      as well as some random index to leave out of the new list
    print ("The new list is", print_except_given_argument(main_list,random.randint(0,len(main_list)-1)))

#invoke main
main()