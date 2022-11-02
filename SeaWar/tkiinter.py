from tkinter import*
from random import*
root = Tk()
root.title("War at the Sea")

fieldSize = 500


c = Canvas(root, width=fieldSize+10, height=fieldSize+10, background="white")
cellSize = 50

c.pack()
for i in range(5, 555, 50):
    c.create_line(i, 5, i, 505)
for i in range(5, 555, 50):
    c.create_line(5, i, 505, i)
for i in range(10):
    corx = randint(1, 10)
    cory = randint(1, 10)
    c.create_rectangle(((corx - 1) * 50) +5, ((cory - 1)  * 50) +5, ((corx - 1) * 50) +55, ((cory - 1)  * 50) + 55, fill="red")
root.mainloop()