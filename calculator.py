from tkinter import *
from math import *

OPERATOR = None
NUM = None
NUM1 = None
NUM2 = None

root = Tk()
root.title("Simple Calculator")
root.resizable(False, False)

e = Entry(root, width=50, borderwidth=0)
e.grid(row=0, column=0, columnspan=4, padx=0, pady=0)

e.configure(bg='#737373')


def get_NUM():
    if "." in e.get():
        num = float(e.get())
    else:
        num = int(e.get())
    return num


def delete_last_char():
    current = e.get()
    l = len(current) - 1
    new = current[0:l]
    e.delete(0, END)
    e.insert(0, new)
    global NUM
    if "." in e.get():
        NUM = float(e.get())
    else:
        NUM = int(e.get())


def clear():
    global OPERATOR
    global NUM
    global NUM1
    global NUM2
    OPERATOR = None
    NUM = None
    NUM1 = None
    NUM2 = None
    e.delete(0, END)


def button_click(number):
    current = e.get()
    num = str(current) + str(number)
    e.delete(0, END)
    e.insert(0, num)


def get_operators(opr):
    global OPERATOR
    OPERATOR = opr
    global NUM1
    NUM1 = get_NUM()
    e.delete(0, END)


def calculate():
    global NUM
    global NUM2
    if OPERATOR == "addition":
        NUM2 = get_NUM()
        e.delete(0, END)
        result = NUM1 + NUM2
        e.delete(0, END)
        e.insert(0, result)
    elif OPERATOR == "subtraction":
        NUM2 = get_NUM()
        result = NUM1 - NUM2
        e.delete(0, END)
        e.insert(0, result)
    elif OPERATOR == "multiplication":
        NUM2 = get_NUM()
        result = NUM1 * NUM2
        e.delete(0, END)
        e.insert(0, result)
    elif OPERATOR == "divide":
        NUM2 = get_NUM()
        result = NUM1 / NUM2
        e.delete(0, END)
        e.insert(0, result)
    elif OPERATOR == "percentage":
        NUM = NUM1
        result = NUM / 100
        e.delete(0, END)
        e.insert(0, result)
    elif OPERATOR == "square":
        NUM = NUM1
        result = NUM ** 2
        e.delete(0, END)
        e.insert(0, result)
    elif OPERATOR == "squareroot":
        NUM = NUM1
        result = sqrt(NUM)
        e.delete(0, END)
        e.insert(0, result)
    elif OPERATOR == "inverse":
        NUM = NUM1
        result = 1 / NUM
        e.delete(0, END)
        e.insert(0, result)


button_1 = Button(root, text="1", height=3, width=10, bg='#0d0d0d', fg='white', command=lambda: button_click(1))
button_2 = Button(root, text="2", height=3, width=10, bg='#0d0d0d', fg='white', command=lambda: button_click(2))
button_3 = Button(root, text="3", height=3, width=10, bg='#0d0d0d', fg='white', command=lambda: button_click(3))
button_4 = Button(root, text="4", height=3, width=10, bg='#0d0d0d', fg='white', command=lambda: button_click(4))
button_5 = Button(root, text="5", height=3, width=10, bg='#0d0d0d', fg='white', command=lambda: button_click(5))
button_6 = Button(root, text="6", height=3, width=10, bg='#0d0d0d', fg='white', command=lambda: button_click(6))
button_7 = Button(root, text="7", height=3, width=10, bg='#0d0d0d', fg='white', command=lambda: button_click(7))
button_8 = Button(root, text="8", height=3, width=10, bg='#0d0d0d', fg='white', command=lambda: button_click(8))
button_9 = Button(root, text="9", height=3, width=10, bg='#0d0d0d', fg='white', command=lambda: button_click(9))
button_0 = Button(root, text="0", height=3, width=10, bg='#0d0d0d', fg='white', command=lambda: button_click(0))

button_mul = Button(root, text="*", height=3, width=10, bg='#333333', fg='white', command=lambda: get_operators("multiplication"))
button_sub = Button(root, text="-", height=3, width=10, bg='#333333', fg='white', command=lambda: get_operators("subtraction"))
button_add = Button(root, text=u'\u002B', height=3, width=10, bg='#333333', fg='white', command=lambda: get_operators("addition"))
button_eq = Button(root, text="=", height=3, width=10, bg='#e69900', fg='white', command=lambda: calculate())
button_alt = Button(root, text=u'\u00B1', height=3, width=10, bg='#0d0d0d', fg='white', command=lambda: get_operators(""))
button_dot = Button(root, text=".", height=3, width=10, bg='#0d0d0d', fg='white', command=lambda: button_click("."))
button_reminder = Button(root, text="%", height=3, width=10, bg='#333333', fg='white', command=lambda: get_operators("percentage"))
button_CE = Button(root, text="CE", height=3, width=10, bg='#333333', fg='white', command=lambda: get_operators("CE"))
button_clear = Button(root, text="C", height=3, width=10, bg='#333333', fg='white', command=clear)
button_delete = Button(root, text=u'\u232B', height=3, width=10, bg='#333333', fg='white', command=lambda: delete_last_char())
button_inverse = Button(root, text="1/x", height=3, width=10, bg='#333333', fg='white', command=lambda: get_operators("inverse"))
button_square = Button(root, text="x²", height=3, width=10, bg='#333333', fg='white', command=lambda: get_operators("square"))
button_squareroot = Button(root, text="√x", height=3, width=10, bg='#333333', fg='white', command=lambda: get_operators("squareroot"))
button_div = Button(root, text=u'\u00F7', height=3, width=10, bg='#333333', fg='white', command=lambda: get_operators("divide"))

button_reminder.grid(row=1, column=0)
button_CE.grid(row=1, column=1)
button_clear.grid(row=1, column=2)
button_delete.grid(row=1, column=3)

button_inverse.grid(row=2, column=0)
button_square.grid(row=2, column=1)
button_squareroot.grid(row=2, column=2)
button_div.grid(row=2, column=3)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_mul.grid(row=3, column=3)

button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)
button_sub.grid(row=4, column=3)

button_1.grid(row=5, column=0)
button_2.grid(row=5, column=1)
button_3.grid(row=5, column=2)
button_add.grid(row=5, column=3)

button_alt.grid(row=6, column=0)
button_0.grid(row=6, column=1)
button_dot.grid(row=6, column=2)
button_eq.grid(row=6, column=3)

root.configure(bg='#737373')
root.mainloop()
