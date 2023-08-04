from tkinter import *
root = Tk()
root.title('Calculator')
root.geometry('1800x1900')
root.config(bg='#335594')

lab1 = Label(root,text = 'Enter the first number:', bg='#335594', fg='black', font ='Monsterrat, 30')
lab1.grid(row=0, column=0, padx=20, pady=20)

inp1 = Entry(root,width=20)
inp1.grid(row=0, column=1, padx=5, pady=20)

lab2 = Label(root, text='Enter the second number:', bg='#335594', fg='black', font ='Monsterrat, 30')
lab2.grid(row=1, column=0, padx=20)

inp2 = Entry(root, width=20)
inp2.grid(row=1, column=1, padx=5)

lab3 = Label(root, text='Answer:', bg='#335594', fg='black', font='Monsterrat, 30')
lab3.grid(row=2, column=0, padx=5, pady=20)

ent_ans = Text(root, height=8, width=30, font='Monsterrat,40')
ent_ans.grid(row=2, column=1, pady=1,)

def add():
    num1_str = inp1.get()
    num2_str = inp2.get()
    try:
        num1 = int(num1_str)
        num2 = int(num2_str)
    except ValueError:
        er_ans = 'Please enter valid numbers in both spaces'
        ent_ans.insert('0.0',er_ans)
        return
    answer = num1 + num2
    ent_ans.insert('0.0',str(answer))


def sub():
    num1_str = inp1.get()
    num2_str = inp2.get()
    try:
        num1 = int(num1_str)
        num2 = int(num2_str)
    except ValueError:
        er_ans = 'Please enter valid numbers in both spaces'
        ent_ans.insert('0.0', er_ans)
        return
    answer = num1 - num2
    ent_ans.insert('0.0', str(answer))

def mul():
    num1_str = inp1.get()
    num2_str = inp2.get()
    try:
        num1 = int(num1_str)
        num2 = int(num2_str)
    except ValueError:
        er_ans = 'Please enter valid numbers in both spaces'
        ent_ans.insert('0.0', er_ans)
        return
    answer = num1*num2
    ent_ans.insert('0.0', str(answer))

def div():
    num1_str = inp1.get()
    num2_str = inp2.get()
    try:
        num1 = int(num1_str)
        num2 = int(num2_str)
    except ValueError:
        er_ans = 'Please enter valid numbers in both spaces'
        ent_ans.insert('0.0', er_ans)
        return
    answer = num1/num2
    ent_ans.insert('0.0', str(answer))

def exp():
    num1_str = inp1.get()
    num2_str = inp2.get()
    try:
        num1 = int(num1_str)
        num2 = int(num2_str)
    except ValueError:
        er_ans = 'Please enter valid numbers in both spaces'
        ent_ans.insert('0.0', er_ans)
        return
    answer = num1**num2
    ent_ans.insert('0.0', str(answer))
def clear():
    inp1.delete(0,END)
    inp2.delete(0,END)
    ent_ans.delete('0.0',END)




btn1 = Button(root, text='Addition', bg='#335594', fg='black', command=add, font='Monsterrat, 30')
btn1.grid(row=3, column=0, padx=5, pady=5)
btn2 = Button(root, text='Subtraction', bg='#335594', fg='black', command=sub, font='Monsterrat, 30')
btn2.grid(row=3, column=1, padx=5, pady=5)
btn3 = Button(root, text='Multiplication', bg='#335594',fg='black', command=mul, font='Monsterrat, 30')
btn3.grid(row=4, column=0, padx=5, pady=5)
btn4 = Button(root, text='Division', bg='#335594', fg='black', command=div,  font='Monsterrat, 30')
btn4.grid(row=4, column=1, padx=5, pady=5)
btn5 = Button(root, text='Exponential', bg='#335594', fg='black', command=exp, font='Monsterrat, 30')
btn5.grid(row=5, column=0, padx=5, pady=5)
btn6 = Button(root, text='Clear', bg='#335594', fg='black', command=clear, font='Monsterrat, 30')
btn6.grid(row=6, columnspan=3, padx=5)

root.mainloop()