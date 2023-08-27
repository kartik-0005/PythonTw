import tkinter as tk

def clickbutton():
    root.title("changed")
root=tk.Tk()
root.title("Calculator")
root.geometry("300x300")
l=tk.Label(root,padx=10,pady=10,text="Program to change title")
l.pack()
button1=tk.Button(root,text="click me",padx=10,pady=10,command=clickbutton)
button1.pack()
root.mainloop()