import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.entry = tk.Entry(root, width=20, font=('Arial', 18))
        self.entry.grid(row=0, column=0, columnspan=4)
        self.equation = ''
        self.result = None

        
        #create buttons and specify their position on the screen
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]
        buttoncount = 0
        for row in range(3):
            for column in range(3):
                buttoncount += 1
                tk.Button(root,text = str(buttoncount)).grid(row=row,column=column)
        

    def on_button_click(self, value):
        self.equation += value
        self.update_entry()

    #method to clear the entry.
    def clear(self):
        self.equation = ''
        self.update_entry()

    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.equation)

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

       

   

def main():
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()


main()