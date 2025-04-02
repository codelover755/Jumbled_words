from tkinter import * 
import random
from tkinter import messagebox

words = {
    "apple":"papel","mango":"oangm",\
        "achieve":"hveecia"
}

window = Tk()
window.config(bg="yellow")

current_word = ""
correct_answer = ""
points = 0
def new_word():
    global current_word,correct_answer
    correct_answer,current_word = random.choice(list(words.items()))
    print(current_word,correct_answer)
    label.config(text=current_word,font=("Helvetica",20),fg="blue",bg="yellow")

def check_answer():
    global correct_answer,points
    print(correct_answer)
    a = answer_entry.get()
    if correct_answer == a:
        messagebox.showinfo("win","This is correct")
        answer_entry.delete(0,END)
        points = points + 1
        display.config(text=str(points))
        new_word()
    else:
        messagebox.showerror("loose","try again")
        answer_entry.delete(0,END)

def show_ans():
    global correct_answer, points
    messagebox.showinfo("Answer","The answer is {}".format(correct_answer))
    points -= 1
    display.config(text=str(points))
    new_word()

label = Label(window,text="")
answer_entry = Entry(window)
answer = Button(window,text="Click this to answer", command=check_answer,font="consolas",bg="red",fg="white")
new_word()
display = Label(window,text="")
print(points)
reset_button = Button(window,text="Change word",command=new_word,font="consolas",bg="white",fg="red")
show_answer = Button(window,text="Show answer",command=show_ans,font="consolas",bg="white",fg="green")

display.pack()
label.pack()
answer_entry.pack()
answer.pack()
reset_button.pack()
show_answer.pack()
window.mainloop()
