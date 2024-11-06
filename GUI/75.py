#Write a Python GUI program to create a Checkbutton widget using tkinter module and display its value through label on a button click
import tkinter as tk

def show():
    value = var.get()
    label.config(text=f"Checkbutton value: {'checked' if value else 'unchecked'}")

root = tk.Tk()
root.title("CheckButton")

var = tk.IntVar()

# checkbutton widget
checkbutton = tk.Checkbutton(root, text="Click me", variable=var)
checkbutton.pack()

# label widget to  display value
label = tk.Label(root, text="Checkbutton value: Unchecked")
label.pack()

# button
button = tk.Button(root, text="Show value", command=show)
button.pack()

root.mainloop()