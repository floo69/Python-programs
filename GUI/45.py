#45. Design GUI to input marks in 3 subjects and print grade on a button click 

import tkinter as tk
def grade():
    mark1 = int(entry1.get())
    mark2 = int(entry2.get())
    mark3 = int(entry3.get())
    total = mark1+mark2+mark3

    if total>90:
        a.config(text="Grade A")
    elif total >75 and total <= 90:
        a.config(text="Grade B")
    else:
        a.config(text="Grade C")

root = tk.Tk()
root.title("Grade Calci")

# input
entry1 = tk.Entry(root, width=10)
entry1.grid(row=0, column=1, padx=5, pady=5)

entry2 = tk.Entry(root, width=10)
entry2.grid(row=1, column=1, padx=5, pady=5)

entry3 = tk.Entry(root, width=10)
entry3.grid(row=2, column=1, padx=5, pady=5)

# label
label1 = tk.Label(root, text="Mark 1")
label1.grid(row=0, column=0, padx=5, pady=5)

label2 = tk.Label(root, text="Mark 2")
label2.grid(row=1, column=0, padx=5, pady=5)

label3 = tk.Label(root, text="Mark 3")
label3.grid(row=2, column=0, padx=5, pady=5)

a = tk.Label(root, text="Result")
a.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

but = tk.Button(root, text="Calculate", command=grade)
but.grid(row=3, column=0, padx=5, pady=5)

root.mainloop()


