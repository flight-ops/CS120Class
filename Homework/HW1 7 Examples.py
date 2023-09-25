#Number 7

#Example of using a global variable

my_global_variable = 0


#this function can call my_global_variable, because it is a global variable
#it can also call my_local_variable, because it is inside the function
def increase_global_count():
    global my_global_variable 
    my_global_variable += 1
    #my_local_variable = my_global_variable + 1
    print (my_global_variable)

#this one checks the global and local variables
#def check_counts():
    #checks for global variable value
    #if my_global_variable == 1:
        #print("I can see the global variable")
    #else:
        #print("I cannot see the global variable")
        
    #checks for local variable value
    #if my_local_variable == 1:
        #print("I can see the local variable")
    #else:
        #print("I cannot see the local variable")

#increase_global_count()
#check_counts()