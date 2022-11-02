from tkinter import*
root = Tk()
root.title("War at the Sea")
c = Canvas(root, width=510, height=510, background="white")
c.pack()
for i in range(5, 555, 50):
    c.create_line(i, 5, i, 505)

root.mainloop()