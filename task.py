import customtkinter as ctk


root = ctk.CTk()
root.geometry("450x750")
root.title("Task")


def add_task():


    task=entry.get()
    label=ctk.CTkLabel(scroloble,text=task ,text_color="red")
    label.pack()
    entry.delete(0,ctk.END)




title_label=ctk.CTkLabel(root,text="Daily Task" ,text_color="red",font=ctk.CTkFont(size=30,weight="bold") )
title_label.pack(padx=10,pady=10)



scroloble=ctk.CTkScrollableFrame(root,fg_color="pink", height=500,width=500)
scroloble.pack(padx=10,pady=10)

entry=ctk.CTkEntry(scroloble, text_color="red",placeholder_text="enter your txt")
entry.pack(fill="x")


button=ctk.CTkButton(root,text="add",command=add_task,hover_color="darkblue")
button.pack(padx=10,pady=10)
root.mainloop()