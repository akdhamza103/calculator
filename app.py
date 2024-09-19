import tkinter as tk

win = tk.Tk()

def get_values(entry_x, entry_y):
    try:
        x = float(entry_x.get())
        y = float(entry_y.get())
        return x, y
    except ValueError:
        tk.Label(win, text="Please enter valid numbers").grid(row=5, column=0, columnspan=5)

def addition():
    x, y = get_values(entry_x_add, entry_y_add)
    if x is not None and y is not None:
        result = x + y
        tk.Label(win, text=f"Answer: {result}").grid(row=1, column=4)

def substract():
    x, y = get_values(entry_x_sub, entry_y_sub)
    if x is not None and y is not None:
        result = x - y
        tk.Label(win, text=f"Answer: {result}").grid(row=2, column=4)

def multiplication():
    x, y = get_values(entry_x_mul, entry_y_mul)
    if x is not None and y is not None:
        result = x * y
        tk.Label(win, text=f"Answer: {result}").grid(row=3, column=4)

def division():
    x, y = get_values(entry_x_div, entry_y_div)
    if x is not None and y is not None:
        if y != 0:
            result = x / y
            tk.Label(win, text=f"Answer: {result}").grid(row=4, column=4)
        else:
            tk.Label(win, text="Cannot divide by zero").grid(row=5, column=0, columnspan=5)

tk.Label(win, text="Calculator", font="bold").grid(row=0, column=0, columnspan=5)

# Addition
tk.Label(win, text="Addition").grid(row=1, column=0)
entry_x_add = tk.Entry(win)
entry_x_add.grid(row=1, column=1)
entry_y_add = tk.Entry(win)
entry_y_add.grid(row=1, column=2)
tk.Button(win, text="Okay", command=addition).grid(row=1, column=3)

# Subtraction
tk.Label(win, text="Subtraction").grid(row=2, column=0)
entry_x_sub = tk.Entry(win)
entry_x_sub.grid(row=2, column=1)
entry_y_sub = tk.Entry(win)
entry_y_sub.grid(row=2, column=2)
tk.Button(win, text="Okay", command=substract).grid(row=2, column=3)

# Multiplication
tk.Label(win, text="Multiplication").grid(row=3, column=0)
entry_x_mul = tk.Entry(win)
entry_x_mul.grid(row=3, column=1)
entry_y_mul = tk.Entry(win)
entry_y_mul.grid(row=3, column=2)
tk.Button(win, text="Okay", command=multiplication).grid(row=3, column=3)

# Division
tk.Label(win, text="Division").grid(row=4, column=0)
entry_x_div = tk.Entry(win)
entry_x_div.grid(row=4, column=1)
entry_y_div = tk.Entry(win)
entry_y_div.grid(row=4, column=2)
tk.Button(win, text="Okay", command=division).grid(row=4, column=3)

win.mainloop()