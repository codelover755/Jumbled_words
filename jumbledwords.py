from email import message
from tkinter import * 
import random
from tkinter import messagebox
from turtle import color

words = {
    "apple":"papel","mango":"oangm","achieve":"hveecia"
}

window = Tk()
window.config(bg="yellow")

current_answer = ""
current_word = ""
def new_word():
    global current_answer, current_word
    correct_answer,current_word = random.choice(list(words.items()))
    print(current_word,correct_answer)
    label.config(text=current_word,font=("Helvetica",20),fg="blue",bg="yellow")

def check_answer():
    global current_answer
    a = answer_entry.get()
    if current_answer == a:
        messagebox.showinfo("win","This is correct")
    else:
        messagebox.showerror("loose","try again")
label = Label(window,text="")
answer_entry = Entry(window)
answer = Button(window,text="Click this to answer", command=check_answer,font="consolas",bg="red",fg="white")
new_word()

label.pack()
answer_entry.pack()
answer.pack()
window.mainloop()