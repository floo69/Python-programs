# Design GUI to place 10 buttons using grid

import tkinter as tk

root = tk.Tk()
root.title("Button Grid")

for i in range(2):
    for j in range(5):
        button = tk.Button(root, text=f"Button = {i*5+j+1}")
        button.grid(row=i, column=j, padx=5, pady=5)

root.mainloop()
