import random
#create a function to load a list
def create_list():
    local_list = []
    for i in range (random.randint(1,20)):
        local_list.append(random.randint(0,10))
    print ("The locally generated list is:", local_list)
    return local_list

#create a function to print all values in the list,
#except at the index passed in an argument

def print_except_given_argument(main_list, excepted_index):
    print("Changing list...")
    print("The excepted index is:", excepted_index)
    #placeholder list
    new_local_list = []
    
    for entry in range(len(main_list)):
        #check if index is excepted, if not, append to new list, if so, print a message for the user. 
        if entry != excepted_index:
            new_local_list.append(main_list[entry])
        elif entry == excepted_index:
            print ("excluding", main_list[entry],"at index", entry)

    return new_local_list
        

def main():
    main_list = []
    main_list = create_list()
    print ("The original list is:", main_list)
    print ("The new list is", print_except_given_argument(main_list,random.randint(0,len(main_list)-1)))
main()