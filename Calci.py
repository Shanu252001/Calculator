import tkinter
from tkinter import *


expression=""
def clear():
    global expresssion
    expresssion = ""
    equation.set("")


def show(num):
    global expression
    expression=expression+str(num)
    equation.set(expression)

def cal():
    try:
        global expression
        total=str(eval(expression))
        equation.set(total)
        expression=""
    except:
        equation.set("error")
        expression = ""

if __name__=="__main__":
    root=tkinter.Tk()
    root.title("Calculator")
    root.geometry("500x500")
    root.resizable(False,False)
    root.configure(bg="black")
    equation=StringVar()
    enter_entry=Entry(root,textvariable=equation)
    enter_entry.grid(columnspan=4,ipadx=200,ipady=10)
    cbutton=Button(root,width=10,height=3,background="orange",bd=5,text="C",pady=2,font=("Arial",10,"bold"),command=clear).grid(row=2,column=0)
    hashbutton = Button(root, width=10, height=3, background="grey", bd=5, text="/", pady=2,font=("Arial", 10, "bold"),command=lambda :show("/")).grid(row=2, column=1)
    perbutton = Button(root, width=10, height=3, background="grey", bd=5, text="%", pady=2,font=("Arial", 10, "bold"),command=lambda :show("%")).grid(row=2, column=2)
    starbutton = Button(root, width=10, height=3, background="grey", bd=5, text="*", pady=2,font=("Arial", 10, "bold"),command=lambda :show("*")).grid(row=2, column=3)

    sevenbutton = Button(root, width=10, height=3, background="grey", bd=5, text="7", pady=2,
                     font=("Arial", 10, "bold"),command=lambda :show(7)).grid(row=3, column=0)
    eightbutton = Button(root, width=10, height=3, background="grey", bd=5, text="8", pady=2,
                        font=("Arial", 10, "bold"),command=lambda :show(8)).grid(row=3, column=1)
    ninebutton = Button(root, width=10, height=3, background="grey", bd=5, text="9", pady=2,
                       font=("Arial", 10, "bold"),command=lambda :show(9)).grid(row=3, column=2)
    minusbutton = Button(root, width=10, height=3, background="grey", bd=5, text="-", pady=2,
                        font=("Arial", 10, "bold"),command=lambda :show("-")).grid(row=3, column=3)

    fourbutton = Button(root, width=10, height=3, background="grey", bd=5, text="4", pady=2,
                         font=("Arial", 10, "bold"), command=lambda: show(4)).grid(row=4, column=0)
    fivebutton = Button(root, width=10, height=3, background="grey", bd=5, text="5", pady=2,
                         font=("Arial", 10, "bold"), command=lambda: show(5)).grid(row=4, column=1)
    sixbutton = Button(root, width=10, height=3, background="grey", bd=5, text="6", pady=2,
                        font=("Arial", 10, "bold"), command=lambda: show(6)).grid(row=4, column=2)
    plusbutton = Button(root, width=10, height=3, background="grey", bd=5, text="+", pady=2,
                         font=("Arial", 10, "bold"), command=lambda: show("+")).grid(row=4, column=3)

    onebutton = Button(root, width=10, height=3, background="grey", bd=5, text="1", pady=2,
                        font=("Arial", 10, "bold"), command=lambda: show(1)).grid(row=5, column=0)
    twobutton = Button(root, width=10, height=3, background="grey", bd=5, text="2", pady=2,
                        font=("Arial", 10, "bold"), command=lambda: show(2)).grid(row=5, column=1)
    threebutton = Button(root, width=10, height=3, background="grey", bd=5, text="3", pady=2,
                       font=("Arial", 10, "bold"), command=lambda: show(3)).grid(row=5, column=2)
    equalbutton = Button(root, width=10, height=3, background="red", bd=5, text="=", pady=2,
                        font=("Arial", 10, "bold"), command=lambda: cal()).grid(row=5, column=3)

    zerobutton = Button(root, width=10, height=3, background="grey", bd=5, text="0", pady=2,
                       font=("Arial", 10, "bold"), command=lambda: show(0)).grid(row=6, column=0)
    decimalbutton = Button(root, width=10, height=3, background="grey", bd=5, text=".", pady=2,
                       font=("Arial", 10, "bold"), command=lambda: show(".")).grid(row=6, column=1)



    root.mainloop()


