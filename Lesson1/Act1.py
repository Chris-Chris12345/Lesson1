from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Button")
root.config(background="blue")

#creating a label
btn = Label(root,text="Click me!",bd="50").place(x=200,y=200)
btn2 = Label(root,text="Hello").place(x=100,y=100)

root.mainloop()