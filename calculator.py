import tkinter as tk
import math

# Evaluate the expression entered
def evaluate_expression():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Add input to entry box
def press(key):
    entry.insert(tk.END, key)

# Clear the entry box
def clear():
    entry.delete(0, tk.END)

# Special scientific functions
def calculate_func(func):
    try:
        value = float(entry.get())
        entry.delete(0, tk.END)
        if func == 'sqrt':
            entry.insert(tk.END, math.sqrt(value))
        elif func == 'sin':
            entry.insert(tk.END, math.sin(math.radians(value)))
        elif func == 'cos':
            entry.insert(tk.END, math.cos(math.radians(value)))
        elif func == 'tan':
            entry.insert(tk.END, math.tan(math.radians(value)))
        elif func == 'log':
            entry.insert(tk.END, math.log10(value))
        elif func == 'ln':
            entry.insert(tk.END, math.log(value))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# GUI setup
root = tk.Tk()
root.title("Scientific Calculator")
entry = tk.Entry(root, width=30, borderwidth=5, font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Buttons layout
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3), ('sqrt',1,4),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3), ('log',2,4),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3), ('ln',3,4),
    ('0',4,0), ('.',4,1), ('+',4,2), ('=',4,3), ('C',4,4),
    ('sin',5,0), ('cos',5,1), ('tan',5,2), ('(',5,3), (')',5,4)
]

for (text, r, c) in buttons:
    if text == '=':
        tk.Button(root, text=text, width=5, height=2, command=evaluate_expression).grid(row=r, column=c)
    elif text == 'C':
        tk.Button(root, text=text, width=5, height=2, command=clear).grid(row=r, column=c)
    elif text in ['sqrt', 'sin', 'cos', 'tan', 'log', 'ln']:
        tk.Button(root, text=text, width=5, height=2, command=lambda t=text: calculate_func(t)).grid(row=r, column=c)
    else:
        tk.Button(root, text=text, width=5, height=2, command=lambda t=text: press(t)).grid(row=r, column=c)

root.mainloop()
