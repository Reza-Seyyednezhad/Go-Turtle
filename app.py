import turtle as tl
from tkinter import *

root = Tk()
root.geometry("500x300")
root.resizable(False, False)
root.title('Setting')
# ----------------------------------------
InputBGColorValue = StringVar()
BgColor = Label(root, text= "Background Color(ex.: #000): ", font=("Arial", 18))
InputBGColor = Entry(root, font=("Arial", 18))
BgColor.grid(row=1, column=1)
InputBGColor.grid(row=1, column=2)
# -----------------------------------------
FgColor = Label(root, text= "Color(ex.: #000): ", font=("Arial", 18))
InputColor = Entry(root, font=("Arial", 18))
FgColor.grid(row=2, column=1)
InputColor.grid(row=2, column=2)
# ----------------------------------------
fontSize = Label(root, text= "Font Size(ex.: 5): ", font=("Arial", 18))
InputFont = Entry(root, font=("Arial", 18))
fontSize.grid(row=3, column=1)
InputFont.grid(row=3, column=2)
# --------------------------------------------------
moveLength = Label(root, text= "Move Length(ex.: 50): ", font=("Arial", 18))
InputMove = Entry(root, font=("Arial", 18))
moveLength.grid(row=4, column=1)
InputMove.grid(row=4, column=2)
# --------------------------------------------------
F1Label = Label(root, text= "Pen Up: 'F1'", font=("Arial", 10)).grid(row=6, column=1)
F2Label = Label(root, text= "Pen Down: 'F2'", font=("Arial", 10)).grid(row=7, column=1)
F3Label = Label(root, text= "Clear: 'F3'", font=("Arial", 10)).grid(row=8, column=1)
F3Label = Label(root, text= "Undo: 'F4'", font=("Arial", 10)).grid(row=9, column=1)


# --------------------------------------------------
def confiq():
    global MOVE_LENGTH
    global move
    bg = InputBGColor.get()
    fg = InputColor.get()
    sz = InputFont.get()
    move = InputMove.get()
    if bg == "" and fg == "" and sz == "" and move == "":
        tl.bgcolor("#000")
        tl.color("#fff")
        tl.pensize(5)
        MOVE_LENGTH = int(50)
        tl.speed(0)
        tl.title('Go Turtle')
        root.destroy()
        app()
    elif isinstance(bg, str) and bg[0] == "#" and isinstance(fg, str) and fg[0] == "#" and isinstance(int(sz), int) and int(sz) in range(1,20) and isinstance(int(move), int) and int(sz) in range(1,100):
        tl.bgcolor(bg)
        tl.color(fg)
        tl.pensize(int(sz))
        MOVE_LENGTH = int(move)
        tl.speed(0)
        tl.title('Go Turtle')
        root.destroy()
        app()
    else: 
        InputBGColor.delete(0, END)
        InputColor.delete(0, END)
        InputFont.delete(0, END)
        InputMove.delete(0, END)
confiqBtn = Button(root, command= confiq, text="Run", padx=10, pady=10, justify='center' , font=("Arial", 18))
confiqBtn.grid(row=5, column=1)

def to_up():
    tl.seth(90)
    tl.fd(MOVE_LENGTH)

def to_down():
    tl.seth(270)
    tl.fd(MOVE_LENGTH)


def to_right():
    tl.seth(0)
    tl.fd(MOVE_LENGTH)


def to_left():
    tl.seth(180)
    tl.fd(MOVE_LENGTH)

def penup():
    tl.penup()

def pendown():
    tl.pendown()

def clear():
    tl.clear()

def undo():
    tl.undo()
def app():
    tl.onkeypress(to_up, 'Up')
    tl.onkeypress(to_down, 'Down')
    tl.onkeypress(to_right, 'Right')
    tl.onkeypress(to_left, 'Left')
    tl.onkeypress(penup, 'F1')
    tl.onkeypress(pendown, 'F2')
    tl.onkeypress(clear, 'F3')
    tl.onkeypress(undo, 'F4')
    tl.listen(2,2)


if __name__ == "__main__":
    # tl.mainloop()
    root.mainloop()
