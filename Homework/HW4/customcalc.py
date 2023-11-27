import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Eddie's GUI Calculator")
        self.entry = tk.Entry(root, width=20, font=('Arial', 18))
        
        #create buttons and specify their position on the screen
        buttons = [  
            "7", "8", "9", 
            "4", "5", "6", 
            "1", "2", "3", 
            "0", ".", "=", 
            
        ]
        # [ 
        #     ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        #     ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        #     ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        #     ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
        # ]
        row_count = 1
        col_count = 0

        for button in buttons:
            tk.Button(root, text=button, font=('Arial', 12))
            if col_count > 3:
                col_count = 0
                row_count += 1
    
    def on_button_click(self, value):
        self.equation += value
        self.update_entry()

    #method to clear the current entry
    def clear(self):
        self.equation = ''
        self.update_entry()

    #method to change the current entry.
    def update_entry(self):
        #remove outdated entry
        self.entry.delete(0, tk.END)
        #insert current entry (self.equation)
        self.entry.insert(tk.END, self.equation)

    #attempt to evaluate equation
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