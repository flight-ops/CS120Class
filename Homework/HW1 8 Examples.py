#this function will create a variable to be used as an argument for another function
def function_one():
    my_variable = 1
    print("the current value is:", my_variable)
    #run function to change my_variable
    change_function(my_variable)
    #print value of my_variable
    print("My variable's value is", my_variable)

#this function supposedly changes the value
def change_function(argument):
    print("The value is being changed.")
    argument = 10
    print("The value should now be",argument)

#calling function
function_one()
