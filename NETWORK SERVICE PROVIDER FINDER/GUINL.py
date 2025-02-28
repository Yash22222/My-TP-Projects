from tkinter import *
from phonenumbers import geocoder
from phonenumbers import carrier
import phonenumbers

root = Tk()

details = []

t = Text(root, background='Orange', height=1000, width=1200)
t.insert(END, 'Network Service Provider \n')


def callback():
    details.clear()
    sanNumber = phonenumbers.parse("+919653294869")
    yourLocation = geocoder.description_for_number(sanNumber, "en")
    cname = carrier.name_for_number(sanNumber, "en")
    # a = [i.split(":")[1][1:-1] for i in a if "All User Profile" in i]
    # c = Canvas(root, background='Orange', height=1000, width=1200, cursor='Pencil')
    t.insert(END, yourLocation+'\n')
    t.insert(END, cname)

    t.pack()


f = Frame(root, height=400, width=500)
f.pack()
b = Button(f, text='Show Network Details', width=20, height=3, command=callback)
b.grid(row=1, column=0)
e = Entry(f, width=60)
e.grid(row=1, column=1)
# c = Canvas(root, background='Orange', height=1000, width=1200, cursor='Pencil')
# f = ('Arial', 40, 'bold')
# t = c.create_text(500, 100, text=len(passwords), font=f, fill='gold')
# c.pack()
t.pack()

root.mainloop()
