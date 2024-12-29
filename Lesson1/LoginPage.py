import tkinter as tk

root = tk.Tk()
root.geometry("350x350")
root.title("Login")
root.config(background="red")

username_label= tk.Label(root,text="Username",bd="10").place(x=50,y=50)
password_label = tk.Label(root,text="Password",bd="10").place(x=50,y=100)

username_entry = tk.Entry(root,width=25,font= ("Arial",10)).place(x=150,y=60)
password_entry = tk.Entry(root,width=25,font= ("Arial",10)).place(x=150,y=110)

button = tk.Button(root,text="submit",bd=7).place(x=50,y=150)

root.mainloop()