import tkinter as tk
import math
import matplotlib.pyplot as plt
import numpy as np

# Calculator Functions
def evaluate_expression():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def press(key):
    entry.insert(tk.END, key)

def clear():
    entry.delete(0, tk.END)

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

# Plotting Function
def plot_function():
    plot_window = tk.Toplevel(root)
    plot_window.title("Plot Function")

    tk.Label(plot_window, text="Choose function to plot:").pack()

    func_var = tk.StringVar(value="sin")

    for f in ["sin", "cos", "tan", "log", "exp"]:
        tk.Radiobutton(plot_window, text=f, variable=func_var, value=f).pack(anchor='w')

    def plot():
        func = func_var.get()
        x = np.linspace(-360, 360, 1000)

        if func == "sin":
            y = np.sin(np.radians(x))
        elif func == "cos":
            y = np.cos(np.radians(x))
        elif func == "tan":
            y = np.tan(np.radians(x))
            y[np.abs(y) > 10] = np.nan  # avoid extreme values
        elif func == "log":
            x = np.linspace(0.1, 100, 500)
            y = np.log10(x)
        elif func == "exp":
            x = np.linspace(-10, 10, 500)
            y = np.exp(x)

        plt.plot(x, y)
        plt.title(f"{func}(x)")
        plt.xlabel("x")
        plt.ylabel(f"{func}(x)")
        plt.grid(True)
        plt.show()

    tk.Button(plot_window, text="Plot", command=plot).pack(pady=5)

# GUI Setup
root = tk.Tk()
root.title("Scientific Calculator")

entry = tk.Entry(root, width=30, borderwidth=5, font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Buttons Layout
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3), ('sqrt',1,4),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3), ('log',2,4),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3), ('ln',3,4),
    ('0',4,0), ('.',4,1), ('+',4,2), ('=',4,3), ('C',4,4),
    ('sin',5,0), ('cos',5,1), ('tan',5,2), ('(',5,3), (')',5,4),
    ('Plot',6,0)
]

for (text, r, c) in buttons:
    if text == '=':
        tk.Button(root, text=text, width=5, height=2, command=evaluate_expression).grid(row=r, column=c)
    elif text == 'C':
        tk.Button(root, text=text, width=5, height=2, command=clear).grid(row=r, column=c)
    elif text in ['sqrt', 'sin', 'cos', 'tan', 'log', 'ln']:
        tk.Button(root, text=text, width=5, height=2, command=lambda t=text: calculate_func(t)).grid(row=r, column=c)
    elif text == 'Plot':
        tk.Button(root, text=text, width=25, height=2, command=plot_function).grid(row=r, column=c, columnspan=5)
    else:
        tk.Button(root, text=text, width=5, height=2, command=lambda t=text: press(t)).grid(row=r, column=c)

root.mainloop()
