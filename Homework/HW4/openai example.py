import tkinter as tk


def on_click(event):
    current_text = entry.get()
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create an entry widget to display input and results
entry = tk.Entry(root, font=("Helvetica", 16), justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Define the buttons and their placement
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, font=("Helvetica", 12), command=lambda b=button: on_click(b)).grid(row=row_val, column=col_val, sticky="nsew")
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Configure row and column weights so that they expand proportionally
for i in range(1, 5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Run the main loop
root.mainloop()