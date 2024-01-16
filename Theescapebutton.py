from tkinter import *
from tkinter import messagebox
import random

def yes():
    messagebox.showinfo('', 'Благодарю!')
    quit()

def motionMouse(event):
    btnNo.place(x=random.randint(50, 300), y=random.randint(50, 300))

root = Tk()
root.geometry('550x400')
root.title('Опрос')
root.resizable(width=False, height=False)
root['bg'] = 'white'

label = Label(root, text='Вам понравилось?', font='Arial 14 bold', bg='white')
label.pack()

btnYes = Button(root, text='Да', font='Arial 14 bold', command=yes)
btnYes.place(x=170, y=100)

btnNo = Button(root, text='Нет', font='Arial 14 bold')
btnNo.place(x=350, y=100)
btnNo.bind('<Enter>', motionMouse)

root.mainloop()
