# Write a program to design GUI for calculator which perform addition of two numbers

import tkinter as tk

def addition():
    num1 = float(entry1.get())
    num2 = float(entry2.get())

    result=num1+num2

    res.config(text=f"Result:{result}")

# MAIN WINDOW
root = tk.Tk()
root.title("Calci") 

entry1 = tk.Entry(root, width=10) #input field - where users can type 
entry1.grid(row=0, column=1, padx=5, pady=5)

entry2 = tk.Entry(root, width=10)
entry2.grid(row=1, column=1, padx=5, pady=5)

# create and place Labels - Label used to display messages , instruction or heading
label1 = tk.Label(root, text="Number 1:")
label1.grid(row=0, column=0, padx=5, pady=5)

label2 = tk.Label(root, text="Number 2:")
label2.grid(row=1, column=0, padx=5, pady=5)

# Result Label
res = tk.Label(root, text="Result: ")
res.grid(row=2, column=0, columnspan=2,  padx=5, pady=5)

# Add button
add_b = tk.Button(root, text="Add", command=addition)
add_b.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()