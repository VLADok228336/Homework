from tkinter import*
from random import*
root = Tk()
root.title("War at the Sea")
corsx = {}
corsy = {}
fieldSize = 500


c = Canvas(root, width=fieldSize+10, height=fieldSize+10, background="white")
cellSize = 50

c.pack()
for i in range(5, 555, 50):
    c.create_line(i, 5, i, 505)
for i in range(5, 555, 50):
    c.create_line(5, i, 505, i)
for i in range(4):
    corx = randint(1, 10)
    cory = randint(1, 10)
    if(i != 0):
        if(corsx.__contains__(corx) and corsy.__contains__(cory)):
            i -= 1
            continue
    c.create_rectangle(((corx - 1) * 50) +5, ((cory - 1)  * 50) +5, ((corx - 1) * 50) +55, ((cory - 1)  * 50) + 55, fill="red")
    corsx[i] = corx
    corsy[i] = cory
for i in range(3):
    corx = randint(1, 10)
    cory = randint(1, 10)
    if(i != 0):
        if(corsx.__contains__(corx) and corsy.__contains__(cory)):
            i -= 1
            continue
    c.create_rectangle(((corx - 1) * 50) +5, ((cory - 1)  * 50) +5, ((corx - 1) * 50) +55, ((cory - 1)  * 50) + 55, fill="red")
    corx+=1
    if(corsx.__contains__(corx) and corsy.__contains__(cory) or corsx.__contains__(corx-1) and corsy.__contains__(cory) or corsx.__contains__(corx+1) and corsy.__contains__(cory) or corsx.__contains__(corx) and corsy.__contains__(cory+1) or corsx.__contains__(corx) and corsy.__contains__(cory -1)):
        corx-=2
        if(corsx.__contains__(corx) and corsy.__contains__(cory) or corsx.__contains__(corx-1) and corsy.__contains__(cory) or corsx.__contains__(corx+1) and corsy.__contains__(cory) or corsx.__contains__(corx) and corsy.__contains__(cory+1) or corsx.__contains__(corx) and corsy.__contains__(cory -1)):
            corx+=1
            cory += 1
            if(corsx.__contains__(corx) and corsy.__contains__(cory) or corsx.__contains__(corx-1) and corsy.__contains__(cory) or corsx.__contains__(corx+1) and corsy.__contains__(cory) or corsx.__contains__(corx) and corsy.__contains__(cory+1) or corsx.__contains__(corx) and corsy.__contains__(cory -1)):
                cory-=2
                if(corsx.__contains__(corx) and corsy.__contains__(cory) or corsx.__contains__(corx-1) and corsy.__contains__(cory) or corsx.__contains__(corx+1) and corsy.__contains__(cory) or corsx.__contains__(corx) and corsy.__contains__(cory+1) or corsx.__contains__(corx) and corsy.__contains__(cory -1)):
                    i -= 1
                    continue
                else:
                    c.create_rectangle(((corx - 1) * 50) +5, ((cory - 1)  * 50) +5, ((corx - 1) * 50) +55, ((cory - 1)  * 50) + 55, fill="red")
            else:
                c.create_rectangle(((corx - 1) * 50) +5, ((cory - 1)  * 50) +5, ((corx - 1) * 50) +55, ((cory - 1)  * 50) + 55, fill="red")
        else:
            c.create_rectangle(((corx - 1) * 50) +5, ((cory - 1)  * 50) +5, ((corx - 1) * 50) +55, ((cory - 1)  * 50) + 55, fill="red")
    else:
        c.create_rectangle(((corx - 1) * 50) +5, ((cory - 1)  * 50) +5, ((corx - 1) * 50) +55, ((cory - 1)  * 50) + 55, fill="red")
        corsx[i+4] = corx
        corsy[i+4] = cory
root.mainloop()