import tkinter
from tkinter import *
import random

# questions = [
#     "How many Keywords are there in C Programming language ?",
#     "Which of the following functions takes A console Input in Python ?",
#     "Which of the following is the capital of India ?",
#     "Which of The Following is must to Execute a Python Code ?",
#     "The Taj Mahal is located in  ?",
#     "The append Method adds value to the list at the  ?",
#     "Which of the following is not a costal city of india ?",
#     "Which of The following is executed in browser(client side) ?",
#     "Which of the following keyword is used to create a function in Python ?",
#     "To Declare a Global variable in python we use the keyword ?",
# 

# answers_choice = [
#     ["23","32","33","43",],
#     ["get()","input()","gets()","scan()",],
#     ["Mumbai","Delhi","Chennai","Lucknow",],
#     ["TURBO C","Py Interpreter","Notepad","IDE",],
#     ["Patna","Delhi","Benaras","Agra",],
#     ["custom location","end","center","beginning",],
#     ["Bengluru","Kochin","Mumbai","vishakhapatnam",],
#     ["perl","css","python","java",],
#     ["function","void","fun","def",],
#     ["all","var","let","global",],
# ]

indexes = []
def gen():
    global indexes
    while(len(indexes)<5):
        x=random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append(x)
    print(indexes)

def startQuiz():
    lblQuestions = Label(
        root,
        text= "How many Keywords are there in C Programming language ?",
        font=("Comic sans MS", 20),
        width= 500,
        justify= "center",
        wraplength= 400,
    )
    lblQuestions.pack()

    r1= Radiobutton(
        root,
        text="1978",
        font=("Comic sans MS", 20),
        value= 0,
    )
    r1.pack()

    r2= Radiobutton(
        root,
        text="1968",
        font=("Comic sans MS", 20),
        value= 1,
    )
    r2.pack()

    r3= Radiobutton(
        root,
        text="1979",
        font=("Comic sans MS", 20),
        value= 2,
    )
    r3.pack()

    lblQuestions2 = Label(
        root,
        text= "Which of the following functions takes A console Input in Python ?",
        font=("Comic sans MS", 20),
        width= 500,
        justify= "center",
        wraplength= 400,
    )
    lblQuestions2.pack()

    r1= Radiobutton(
        root,
        text="1978",
        font=("Comic sans MS", 20),
        value= 0,
    )
    r1.pack()

    r2= Radiobutton(
        root,
        text="1968",
        font=("Comic sans MS", 20),
        value= 1,
    )
    r2.pack()

    r3= Radiobutton(
        root,
        text="1979",
        font=("Comic sans MS", 20),
        value= 2,
    )
    r3.pack()

    lblQuestions3 = Label(
        root,
        text= "Which of the following is the capital of India ?",
        font=("Comic sans MS", 20),
        width= 500,
        justify= "center",
        wraplength= 400,
    )
    lblQuestions3.pack()

    r1= Radiobutton(
        root,
        text="1978",
        font=("Comic sans MS", 20),
        value= 0,
    )
    r1.pack()

    r2= Radiobutton(
        root,
        text="1968",
        font=("Comic sans MS", 20),
        value= 1,
    )
    r2.pack()

    r3= Radiobutton(
        root,
        text="1979",
        font=("Comic sans MS", 20),
        value= 2,
    )
    r3.pack()

    lblQuestions4 = Label(
        root,
        text= "The Taj Mahal is located in  ?",
        font=("Comic sans MS", 20),
        width= 500,
        justify= "center",
        wraplength= 400,
    )
    lblQuestions4.pack()

    r1= Radiobutton(
        root,
        text="1978",
        font=("Comic sans MS", 20),
        value= 0,
    )
    r1.pack()

    r2= Radiobutton(
        root,
        text="1968",
        font=("Comic sans MS", 20),
        value= 1,
    )
    r2.pack()

    r3= Radiobutton(
        root,
        text="1979",
        font=("Comic sans MS", 20),
        value= 2,
    )
    r3.pack()

    lblQuestions5 = Label(
        root,
        text= "Which of The Following is must to Execute a Python Code ?",
        font=("Comic sans MS", 20),
        width= 500,
        justify= "center",
        wraplength= 400,
    )
    lblQuestions5.pack()

    r1= Radiobutton(
        root,
        text="1978",
        font=("Comic sans MS", 20),
        value= 0,
    )
    r1.pack()

    r2= Radiobutton(
        root,
        text="1968",
        font=("Comic sans MS", 20),
        value= 1,
    )
    r2.pack()

    r3= Radiobutton(
        root,
        text="1979",
        font=("Comic sans MS", 20),
        value= 2,
    )
    r3.pack()

    lblQuestions6 = Label(
        root,
        text= "The append Method adds value to the list at the  ?",
        font=("Comic sans MS", 20),
        width= 500,
        justify= "center",
        wraplength= 400,
    )
    lblQuestions6.pack()

    r1= Radiobutton(
        root,
        text="1978",
        font=("Comic sans MS", 20),
        value= 0,
    )
    r1.pack()

    r2= Radiobutton(
        root,
        text="1968",
        font=("Comic sans MS", 20),
        value= 1,
    )
    r2.pack()

    r3= Radiobutton(
        root,
        text="1979",
        font=("Comic sans MS", 20),
        value= 2,
    )
    r3.pack()

    lblQuestions7 = Label(
        root,
        text= "Which of the following is not a costal city of india ?",
        font=("Comic sans MS", 20),
        width= 500,
        justify= "center",
        wraplength= 400,
    )
    lblQuestions7.pack()

    r1= Radiobutton(
        root,
        text="1978",
        font=("Comic sans MS", 20),
        value= 0,
    )
    r1.pack()

    r2= Radiobutton(
        root,
        text="1968",
        font=("Comic sans MS", 20),
        value= 1,
    )
    r2.pack()

    r3= Radiobutton(
        root,
        text="1979",
        font=("Comic sans MS", 20),
        value= 2,
    )
    r3.pack()

    lblQuestions8 = Label(
        root,
        text= "Which of the following keyword is used to create a function in Python ?",
        font=("Comic sans MS", 20),
        width= 500,
        justify= "center",
        wraplength= 400,
    )
    lblQuestions8.pack()

    r1= Radiobutton(
        root,
        text="1978",
        font=("Comic sans MS", 20),
        value= 0,
    )
    r1.pack()

    r2= Radiobutton(
        root,
        text="1968",
        font=("Comic sans MS", 20),
        value= 1,
    )
    r2.pack()

    r3= Radiobutton(
        root,
        text="1979",
        font=("Comic sans MS", 20),
        value= 2,
    )
    r3.pack()


    

def bt1Ispressed():
    labelText.destroy()
    bt1.destroy()
    start.destroy()
    startQuiz()
    gen()

root=tkinter.Tk()
root.title("QUIZEE")
root.geometry("1920x1080")
sb = Scrollbar(root)  
sb.pack(side = RIGHT, fill = Y)

labelText= Label(
    root,
    text="QUIZEE",
    font=("Comic sans MS",32,"bold")
)
labelText.pack(pady=(0,50))

start=Entry(root,width=30)
start.pack()
start.insert(10,"enter your name")

# def entryfun():
#     message="Welcome "+name.get()
#     lab1=Label(root,text=message,font=20)
#     lab1.pack()

bt1=Button(root,text="ENTER",command=bt1Ispressed)
bt1.pack()



root.mainloop()