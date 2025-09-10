import random

diferentcolor = ["red", "blue", "green", "yellow"]

for i in range(len(diferentcolor)):
    index = random.randint(0,len(diferentcolor)-1)
    print(diferentcolor[index])

