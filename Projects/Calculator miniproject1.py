#objective: create an interactive calculator

#functions: allow the user to perform all basic operations, +-*/, as well as exponentiation and modulus division


#import math for calculator, because calculator needs math
import math
    
#operation functions declared below

def addition_operation(initial_value, operand_for_addition):
    subtotal = float(initial_value + operand_for_addition)
    return subtotal

def subtraction_operation(initial_value, operand_for_subtraction):
    subtotal = float(initial_value - operand_for_subtraction)
    return subtotal

def multiplication_operation(initial_value, operand_for_multiplication):
    subtotal = float(initial_value * operand_for_multiplication)
    return subtotal

def division_operation(initial_value, operand_for_division):
    if operand_for_division == 0:
        print("Error! Don't divide by zero, math doesn't like that.")
        return initial_value
    
    subtotal = float(initial_value / operand_for_division)

    return subtotal

def modulus_operation(initial_value, operand_for_modulus):
    if operand_for_modulus == 0:
        print("Error! Don't divide by zero, math doesn't like that.")
        return initial_value
    
    subtotal = float(initial_value % operand_for_modulus)
    return subtotal

def exponentiation_operation(initial_value, operand_for_exponentiation):
    subtotal = float(initial_value ** operand_for_exponentiation)
    return subtotal
    
#conversion functions declared below
def decimal_to_hex(integer_input):
    hex_output = hex(int(integer_input))
    return hex_output

def decimal_to_binary(decimal_input):
    binary_output = bin(int(decimal_input))
    return binary_output


        
#function allows user to operate on a running total continuously if they so choose
def primary_operation_loop(initial_value_local_oj):
        #break condition is false, initially
        user_break_condition = False
        subtotal_pol = float(initial_value_local_oj)

        while user_break_condition == False:
            user_chosen_operation = input("Which operation would you like to perform? Choices are: \nadd, subtract, multiply, divide, modulus, exponent, and no_op.\n")
            #if user chooses no_op, no operation will be performed on the initial value. If the user just wants to convert something, they can skip one or two steps and convert directly, rather than
            #adding zero or multiplying by 1

            if user_chosen_operation == "no_op":
                break


            user_second_operand = float(input("What is the second operand?\n"))

            if user_chosen_operation == "add":
                subtotal_pol = addition_operation(subtotal_pol, user_second_operand)
                
            elif user_chosen_operation == "subtract":
                subtotal_pol = subtraction_operation (subtotal_pol, user_second_operand)
                
            elif user_chosen_operation == "multiply":
                subtotal_pol = multiplication_operation(subtotal_pol, user_second_operand)
                
            elif user_chosen_operation == "divide":
                subtotal_pol = division_operation(subtotal_pol, user_second_operand)
                
            elif user_chosen_operation == "modulus":
                subtotal_pol = modulus_operation(subtotal_pol, user_second_operand)
                
            elif user_chosen_operation == "exponent":
                subtotal_pol = exponentiation_operation(subtotal_pol, user_second_operand)
            else:
                print("Unrecognized input. Try again.")
            
            
            print("current subtotal is:", subtotal_pol)

            user_continue_request = input("Would you like to continue performing operations? y/n\n")

            if user_continue_request == "y":
                print("---  continuing loop ---")
                continue
            elif user_continue_request == "n":
                user_break_condition = True
                print("---  breaking loop   ---")
            else:
                user_break_condition = True
                print("---  input unrecognized, breaking    ---")

        return subtotal_pol

#to be used whenever a conversion to integer type is necessary, like in hex/binary conversion functions, or when the user requests an answer in integer form.
#only break loop once the user inputs a valid option, else keep giving them the prompt.
def user_round_prompt(subtotal_urp):

    #flag for checker loop
    valid_input_urp = False
    #notify user of current value
    print("The current value is: ",subtotal_urp,)
    
    while valid_input_urp == False:
        user_round_direction = input("Would you like to round the subtotal up or down to the nearest integer? u/d\nNote: if the value is already an integer, no change will occur.\n" )

        if user_round_direction == "u":
            subtotal_urp = math.ceil(subtotal_urp)
            valid_input_urp = True
        elif user_round_direction == "d":
            subtotal_urp = math.floor(subtotal_urp)
            valid_input_urp = True
        else:
            print("Unrecognized input. Try again.\n")
            continue

    
    return subtotal_urp
def conversion_selection(subtotal_cs):

    user_requested_output_type = input("What form would you like your result in? options are:\nint, float, hex, and binary.\n")

    if user_requested_output_type == "int":
        subtotal_int = user_round_prompt(subtotal_cs)
        total = subtotal_int
    elif user_requested_output_type == "float":
        precision_choice = int(input("How many decimal places would you like to round to? Input a non-zero integer value.\n"))
        total = round(subtotal_cs, precision_choice)

    elif user_requested_output_type == "hex":
        subtotal_int = user_round_prompt(subtotal_cs)
        total = decimal_to_hex(subtotal_int)

    elif user_requested_output_type == "binary":
        subtotal_int = user_round_prompt(subtotal_cs)
        total = decimal_to_binary(subtotal_int)

    return total

#declare main function
def main():
    #prompt user for input
    user_initial_input_main = input("What is your first number?\n")
    #obtain a subtotal value from the primary operation loop
    subtotal_main = primary_operation_loop(user_initial_input_main)
    #ask user if they want to convert, then store it 
    total = conversion_selection(subtotal_main)
    #print ultimate total
    print("Your final value is: ", total)

   
    


user_main_break_condition = False
print("---  Starting Program.   ---")

#allow the user to perform as many individual calculations as they'd like
#end program when user is satisfied
while user_main_break_condition == False:
    main()
    user_continue_request = input("Would you like to make another calculation? y/n\n")
    if user_continue_request == "y":
        continue
    elif user_continue_request == "n":
        print("---  Ending program. ---")
        user_main_break_condition = True
