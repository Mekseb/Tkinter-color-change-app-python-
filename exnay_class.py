from tkinter import *
from random import *
fen1 = Tk()
fen1.geometry("300x300")
can1=Canvas(fen1,width=200,height=200,bg="green")
can1.pack(side=LEFT)
x1, y1, x2, y2 = 10,190,190,10
def drowline():

    global x1,x2,y1,y2,diferent_color

    y2, y1 = y2+10, y1-10
    can1.create_line(x1, y1, x2, y2,width= 2 ,fill="diferent_color" )
    print(x1,x2,y1,y2)



def colorchange():
    diferentcolor=["red","blue","green","yellow"]
    print(diferentcolor)
    for i in range(diferentcolor):
        x = random.randint(i)
        print(diferentcolor[x])


btn=Button(fen1,text = "click me!",command=drowline , font=( "arial",16))
btn.pack(padx=10,pady=10)

btn2= Button(fen1,text = "color-change",command=colorchange, font=( "arial",16))
btn2.pack(side=LEFT)
"""
def drawline():

    global x1, y1, x2, y2, coul
    can1.create_line(x1,y1,x2,y2,width=2,fill=coul)
    y2, y1 = y2+10, y1-10
    print(x1,y1,x2,y2,)
def changecolor():
    global coul

    pal=['purple','cyan','maroon','green','red','blue','orange','yellow']
    c = randrange(8) # => génère un nombre aléatoire de 0 à 7
    coul = pal[c]

x1, y1, x2, y2 = 150, 150, 10, 150

coul = 'dark green'
fen1 = Tk()
# création des widgets "esclaves" :


can1 = Canvas(fen1,bg='dark grey',height=200,width=200)
can1.pack(side=LEFT)


bou1 = Button(fen1,text='Quitter',command=fen1.quit)
bou1.pack(side=BOTTOM)


bou2 = Button(fen1,text='Tracer une ligne',command=drawline)
bou2.pack()



bou3 = Button(fen1,text='Autre couleur',command=changecolor)
bou3.pack()

"""
fen1.mainloop()