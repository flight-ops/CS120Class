#boilerplate code
import tkinter as tk
from tkinter import messagebox

class MyGUI:
    def __init__(self, root):
        self.root = root
        root.title("This is the title!!!")

        self.label = tk.Label(root, text="Enter Text:")
        self.label.pack()

        self.label2 = tk.Label(root, text="another label")
        self.label2.pack()


        self.text_box = tk.Entry(root)
        self.text_box.pack()

        self.checkbox_state = tk.BooleanVar()
        self.checkbox = tk.Checkbutton(root, text="Show in Message Box", variable=self.checkbox_state)
        self.checkbox.pack()

        self.button = tk.Button(root, text="Show Message", command=self.show_message)
        self.button.pack()

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