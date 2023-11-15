#boilerplate code
import tkinter as tk
from tkinter import messagebox

class MyGUI:
    def __init__(self, root):
        self.root = root
        root.title("Eddie's Calculator Project!!!! This is the title!!!")

        self.label = tk.Label(root, text="Enter Item:")
        self.label.pack()

        self.text_box = tk.Entry(root)
        self.text_box.pack()

        self.checkbox_state = tk.BooleanVar()
        self.checkbox = tk.Checkbutton(root, text="Show in Message Box", variable=self.checkbox_state)
        self.checkbox.pack()

        #create button to add an operand

        #create button to add operator

        self.button = tk.Button(root, text="Show Message", command=self.show_message)
        self.button.pack()

        #create button to return a value

        #create a button to clear the total 

    def show_message(self):
        user_input = self.text_box.get()
        if self.checkbox_state.get():
            messagebox.showinfo("Message Box", user_input)
        else:
            print("User Input:", user_input)

root = tk.Tk()
app = MyGUI(root)
root.mainloop()

#customized code

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