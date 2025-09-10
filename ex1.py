import tkinter as tk


root = tk.Tk()

root.geometry("300x300")
root.title("Hello World")
label = tk.Label(root,text= "hello world", font =("arial",10),fg="blue")

label.pack(side="top", padx=10, pady=10)

textbox = tk.Text(root, height=3, font=("arial", 16))
textbox.pack(anchor = "nw", padx=10)

button = tk.Button(root,text="click me!",font=( "arial",16))
button.pack(padx=10,pady=10 )

buttonfrem= tk.Frame(root)
buttonfrem.columnconfigure(0, weight=1)
buttonfrem.columnconfigure(1, weight=1)
buttonfrem.columnconfigure(2, weight=1)
buttonfrem.columnconfigure(7, weight=1)

btn1= tk.Button(buttonfrem,text="1",font=( "arial",16))
btn1.grid(row=0,column=0,sticky=tk.W+tk.E)

btn2= tk.Button(buttonfrem,text="2",font=( "arial",16))
btn2.grid(row=0,column=1,sticky=tk.W+tk.E)

btn3= tk.Button(buttonfrem,text="3",font=( "arial",16))
btn3.grid(row=0,column=2,sticky=tk.W+tk.E)

btn4= tk.Button(buttonfrem,text="4",font=( "arial",16))
btn4.grid(row=1,column=0,sticky=tk.W+tk.E)

btn5= tk.Button(buttonfrem,text="5",font=( "arial",16))
btn5.grid(row=1,column=1,sticky=tk.W+tk.E)

btn6= tk.Button(buttonfrem,text="6",font=( "arial",16))
btn6.grid(row=1,column=2,sticky=tk.W+tk.E)


btn0= tk.Button(buttonfrem,text="0",font=( "arial",16))
btn0.grid(row=2,column=1,sticky=tk.W+tk.E)

btn0= tk.Button(buttonfrem,text="0",font=( "arial",16))
btn0.grid(row=7,column=2,sticky = "ew")

buttonfrem.pack(fill = "x")

root.mainloop()