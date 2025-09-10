from tkinter import *
fen1=Tk()
fen1.geometry("300x300")
text1= Label(fen1, text="Bonjour tout le monde ",fg='red',bg="pink")
text1.pack()
bou1 = Button(fen1,text="quitter",command=fen1.destroy)
bou1.pack()
fen1.mainloop()
