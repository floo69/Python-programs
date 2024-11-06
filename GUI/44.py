# Design GUI to input salary and calculate Gross salary on a button click 

import tkinter as tk

def gross():
    basic = float(entry1.get())
    ha=0.20*basic
    ta=0.10*basic

    result = basic + ha + ta
    res.config(text=f"Result:{result}")

# MAIN WINDOW
root = tk.Tk()
root.title("Gross salary")

# input
entry1 = tk.Entry(root, width=10)
entry1.grid(row=0, column=1, padx=5, pady=5)

# Labels label=tklabel 
label1 = tk.Label(root, text="Baic salary: ")
label1.grid(row=0, column=0, padx=5,pady=5)

res = tk.Label(root, text="Result:")
res.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

but = tk.Button(root, text="Calculate", command=gross)
but.grid(row=1, column=0, padx=5, pady=5)

root.mainloop()