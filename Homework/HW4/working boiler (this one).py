import math
import tkinter as tk


class Calculator:
    def __init__(self, root):
        #define object and a title
        self.root = root
        self.root.title("eddie's super duper (awful) calculator")

        #create entry widget to show input as well as results
        self.entry = tk.Entry(root, width=20, font=('Arial', 18))
        self.entry.grid(row=0, column=0, columnspan=4)

        #create an equation attribute
        self.equation = ''
        self.result = None

    

        #create buttons and specify their position on the screen
        
        buttons = [
                "7", "8", "9", "/",
                "4", "5", "6", "*",
                "1", "2", "3", "-",
                "0", ".", "=", "+",
                "C"
        ]
        #specify intitial condition
        row_count = 1
        column_count = 0

        for button in buttons:
            #make a lambda function and use it as the command parameter
            #when the button is clicked, perform an action with the conditions set in on_button_click
            tk.Button(root,command = lambda b = button : self.on_button_click(b) ,text=button).grid(row=row_count,column=column_count)
            
            #increase the column count each time a button is made (buttons generated from left to right)
            column_count += 1
            
            #when column count exceeds three, move on to the next row and then perform the same action
            if column_count > 3:
                column_count = 0
                row_count +=1   

        #make buttons for the conversion functions
        convertbuttons = [
        "round up","round down", "to hex", "to binary", "to decimal"
        ]
        #add a row
        row_count +=1
        column_count = 0
        for button in convertbuttons:
            tk.Button(root,command = lambda b = button : self.on_button_click(b) ,text=button).grid(row=row_count,column=column_count)
            if column_count < 4:
                column_count+=1
            
            
    #create conditionals for which button does what
    def on_button_click(self, buttonvalue):
        if buttonvalue == "=":
           self.calculate()
        elif buttonvalue == "C":
            self.clear()
        elif buttonvalue == "round up":
            self.round_up()
        elif buttonvalue == "round down":
            self.round_down()
        elif buttonvalue == "to hex":
            self.hex_convert()
        elif buttonvalue == "to binary":
            self.binary_convert()
        elif buttonvalue == "to decimal":
            self.decimal_convert()
            
        else:
            print(buttonvalue)
            self.equation += buttonvalue
            self.update_entry()
            return buttonvalue

    #method to clear the entry.
    def clear(self):
        self.equation = ''
        self.update_entry()

    #removes old entry and inserts new entry
    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.equation)

    #method to actually calculate the given equation
    def calculate(self):
        try:
            self.result = eval(self.equation)
            self.equation = str(self.result)
            self.update_entry()
        except Exception as e:
            self.equation = ''
            self.result = None
            self.update_entry()
            print(f"Error: {e}")

    #round up and down by converting the string to a float, applying a math round operator, converting it back to a string, then updating the screen with a new value.
    def round_up(self):
        self.result = float(self.equation)
        self.result = math.ceil(self.result)
        self.equation = str(self.result)
        self.update_entry()
    def round_down(self):
        self.result = float(self.equation)
        self.result = math.floor(self.result)
        self.equation = str(self.result)
        self.update_entry()


        #convert to hex and binary by first converting to integers, then applying a math function, then updating the screen
    def hex_convert(self):
        self.equation = int(self.equation)
        self.result = hex(self.equation)
        self.equation = str(self.result)
        self.update_entry()

    def binary_convert(self):
        self.equation = int(self.equation)
        self.result = bin(self.equation)
        self.equation = str(self.result)
        self.update_entry()

        #I'm not quite sure what I decided to do here. Why did I change it to an int???
    def decimal_convert(self):
        self.equation = int(self.equation)
        self.result = float(self.equation)
        self.equation = str(self.result)
        self.update_entry()
   

def main():
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()

main()