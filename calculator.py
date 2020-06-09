from tkinter import *
from math import *

root= Tk()
root.title("Simple Calculator")

e=Entry(root, width = 35, borderwidth =5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=20) #columnspan is used to span 3 columns beneath it(the text box)

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    first_number = e.get()
    global f_num  #defining global variable,made global because used in more than one function
    global math #one more global variable
    math = "addition"
    f_num=int(first_number)
    e.delete(0,END)

def button_equal():

    second_number = e.get()
    e.delete(0,END)
    if math == "addition":
        e.insert(0, f_num+int(second_number))
    elif math == "subtraction":
        e.insert(0, f_num-int(second_number))
    elif math == "multiplication":
        e.insert(0, f_num*int(second_number))
    elif math == "subtraction":
        e.insert(0, f_num/int(second_number))
    elif math == "sine":
        e.insert(0,sin(f_num))
    elif math == "cosine":
        e.insert(0,cos(f_num))
    elif math == "tan":
        e.insert(0,tan(f_num))
    elif math == "power":
        e.insert(0, f_num**int(second_number))
    elif math == "reminder":
        e.insert(0, f_num%int(second_number))
    elif math == "floor division":
        e.insert(0, f_num//int(second_number))


def button_subtract():
    first_number = e.get()
    global f_num  #defining global variable,made global because used in more than one function
    global math #one more global variable
    math = "subtraction"
    f_num=int(first_number)
    e.delete(0,END)

def button_multiply():
    first_number = e.get()
    global f_num  #defining global variable,made global because used in more than one function
    global math #one more global variable
    math = "multiplication"
    f_num=int(first_number)
    e.delete(0,END)

def button_divide():
    first_number = e.get()
    global f_num  #defining global variable,made global because used in more than one function
    global math #one more global variable
    math = "division"
    f_num=int(first_number)
    e.delete(0,END)

def button_sin():
    first_number = e.get()
    global f_num  #defining global variable,made global because used in more than one function
    global math #one more global variable
    math = "sine"
    f_num=int(first_number)
    e.delete(0,END)

def button_cos():
    first_number = e.get()
    global f_num  #defining global variable,made global because used in more than one function
    global math #one more global variable
    math = "cosine"
    f_num=int(first_number)
    e.delete(0,END)

def button_tan():
    first_number = e.get()
    global f_num  #defining global variable,made global because used in more than one function
    global math #one more global variable
    math = "tan"
    f_num=int(first_number)
    e.delete(0,END)

def button_pow():
    first_number = e.get()
    global f_num  #defining global variable,made global because used in more than one function
    global math #one more global variable
    math = "power"
    f_num=int(first_number)
    e.delete(0,END)

def button_rem():
    first_number = e.get()
    global f_num  #defining global variable,made global because used in more than one function
    global math #one more global variable
    math = "reminder"
    f_num=int(first_number)
    e.delete(0,END)

def button_floor():
    first_number = e.get()
    global f_num  #defining global variable,made global because used in more than one function
    global math #one more global variable
    math = "floor division"
    f_num=int(first_number)
    e.delete(0,END)


button_1 = Button(root,text="1",padx=40,pady=20,command= lambda: button_click(1),bg="lightyellow")
button_2 = Button(root,text="2",padx=40,pady=20,command= lambda: button_click(2),bg="lightyellow")
button_3 = Button(root,text="3",padx=40,pady=20,command=lambda: button_click(3),bg="lightyellow")
button_4 = Button(root,text="4",padx=40,pady=20,command=lambda: button_click(4),bg="lightyellow")
button_5 = Button(root,text="5",padx=40,pady=20,command=lambda: button_click(5),bg="lightyellow")
button_6 = Button(root,text="6",padx=40,pady=20,command=lambda: button_click(6),bg="lightyellow")
button_7 = Button(root,text="7",padx=40,pady=20,command=lambda: button_click(7),bg="lightyellow")
button_8 = Button(root,text="8",padx=40,pady=20,command=lambda: button_click(8),bg="lightyellow")
button_9 = Button(root,text="9",padx=40,pady=20,command=lambda: button_click(9),bg="lightyellow")
button_0 = Button(root,text="0",padx=40,pady=20,command=lambda: button_click(0),bg="lightyellow")
button_add = Button(root,text="+",padx=39,pady=20,command= button_add,bg="orange")
button_equals = Button(root,text="=",padx=91,pady=20,command= button_equal,bg="lightgreen")
button_clear = Button(root,text="CLEAR",padx=79,pady=20,command= button_clear,bg="skyblue")
button_subtract = Button(root,text="-",padx=40,pady=20,command= button_subtract,bg="orange")
button_multiply = Button(root,text="*",padx=40,pady=20,command= button_multiply,bg="orange")
button_divide = Button(root,text="/",padx=40,pady=20,command= button_divide,bg="orange")
button_sin = Button(root,text="sin",padx=35,pady=20,command= button_sin,bg="pink")
button_cos = Button(root,text="cos",padx=35,pady=20,command= button_cos,bg="pink")
button_tan = Button(root,text="tan",padx=35,pady=20,command= button_tan,bg="pink")
button_pow = Button(root,text="pow",padx=31,pady=20,command= button_pow,bg="orange")
button_rem = Button(root,text="%",padx=38,pady=20,command= button_rem,bg="orange")
button_floor = Button(root,text="//",padx=38,pady=20,command= button_floor,bg="orange")

button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)

button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)

button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)

button_0.grid(row=5,column=0)
button_add.grid(row=6,column=0)
button_equals.grid(row=5,column=1,columnspan=2)
button_clear.grid(row=6,column=1,columnspan=2)

button_subtract.grid(row=7,column=0)
button_multiply.grid(row=7,column=1)
button_divide.grid(row=7,column=2)

button_sin.grid(row=1,column=0)
button_cos.grid(row=1,column=1)
button_tan.grid(row=1,column=2)

button_pow.grid(row=8,column=0)
button_rem.grid(row=8,column=1)
button_floor.grid(row=8,column=2)


root.mainloop()
