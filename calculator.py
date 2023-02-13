from tkinter import *
from tkinter import messagebox

def click(num):
    
    current = entry_val.get()
    entry_val.set(current+num)
    

def clear():
    entry_val.set("")

def equal():
    try:
        current = entry_val.get()
        for i in current:
            if i == "^":
                current =  current.replace("^", "**")
                
        entry_val.set(eval(current))
    except SyntaxError:
        messagebox.showerror("Error", "invalid syntax")
        entry_val.set("")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Float division by zero")
        entry_val.set("")

window = Tk()
window.geometry("445x400")
window.title("Simple calculator")


entry_val = StringVar()
equation_text = Entry(
    window,
    width=35,
    font=12,
    text='',
    bg="#f0eed1",
    textvariable=entry_val
).grid(row=0, column=0, columnspan=4, padx=10, pady=10)


buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "0", "C", "^", "/",
    "(",")","=","%"
]
row = 1
column = 0
for btn in buttons:
    if btn == "C":   
        Button(
            window,
            text=btn,
            font=12,
            padx=20,
            command=clear
        ).grid(row=row, column=column, padx=10, pady=10)
    elif btn == "=":   
        Button(
            window,
            text=btn,
            font=12,
            padx=20,
            command=equal
        ).grid(row=row, column=column, padx=10, pady=10)
        
    else:
        Button(
            window,
            text=btn,
            font=12,
            padx=20,
            command=lambda button=btn: click(button)
        ).grid(row=row, column=column, padx=10, pady=10)
    column+=1
    if column > 3:
        row+=1
        column=0


window.resizable(False,False)
window.mainloop()

