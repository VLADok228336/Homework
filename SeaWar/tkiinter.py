from tkinter import*
from random import*
root = Tk()
root.title("War at the Sea")
c = Canvas(root, width=510, height=510, background="white")
c.pack()
for i in range(5, 555, 50):
    c.create_line(i, 5, i, 505)
for i in range(5, 555, 50):
    c.create_line(5, i, 505, i)
for i in range(10):
    corx = randint(1, 10)
    cory = randint(1, 10)
    c.create_rectangle(corx * 50 +5, cory * 50 +5, corx* 51 -45, cory * 51 - 45, fill="red")
root.mainloop()