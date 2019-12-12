#Made for the sole purpose of GCI-2019
from tkinter import *
import tkinter.messagebox
bclick = True
flag = 0
def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)
def enablebuttton(event):
    if p2.get()=="" or p1.get()=="":
        tkinter.messagebox.showinfo("Name", "Please enter player names.")
    else:
        button1.configure(state=NORMAL)
        button2.configure(state=NORMAL)
        button3.configure(state=NORMAL)
        button4.configure(state=NORMAL)
        button5.configure(state=NORMAL)
        button6.configure(state=NORMAL)
        button7.configure(state=NORMAL)
        button8.configure(state=NORMAL)
        button9.configure(state=NORMAL)
def btnClick(buttons):
    global bclick,flag,p1, p2, pb, pa
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        pb = p2.get() + " Wins!"
        pa = p1.get() + " Wins!"
        checkForWin()
        flag += 1


    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        checkForWin()
        flag += 1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

def newgame1(event):
    global bclick,flag
    bclick = True
    flag = 0
    root.destroy()
    GUI()
def checkForWin():
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] =='X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", pa)

    elif(flag == 8):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")
        disableButton()

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", pb)
def GUI():
    global root,p1,p2,button1,button2,button3,button4,button5,button6,button7,button8,button9
    
    root= Tk()
    root.title("Tic Tac Toe")
    root.config(bg="#220047")
    root.resizable(0,0)
    
    pa=StringVar()
    pb=StringVar()
    p1 = StringVar()
    p2 = StringVar()


    player1_name = Entry(root, textvariable=p1, bd=5)
    player1_name.grid(row=3, column=4)
    
    player2_name = Entry(root, textvariable=p2, bd=5)
    player2_name.grid(row=4, column=4)

    nt1=Button(root,text="New Game",font='roboto 25',bg="#CE9141", fg="#220047")
    nt1.bind("<Button-1>",newgame1)
    nt1.grid(row=5,column=3,columnspan=2)
    
    nt2=Button(root,text="Start Game",font='roboto 25',bg="#CE9141", fg="#220047")
    nt2.bind("<Button-1>",enablebuttton)
    nt2.grid(row=4,rowspan=2,column=3,columnspan=2)

    buttons = StringVar()

    label = Label(root, text="Player Name1:", font='roboto 20',fg="#CE9141", bg="#220047", height=1)
    label.grid(row=3, column=3)


    label = Label(root, text="Player Name2:", font='roboto 20', fg="#CE9141", bg="#220047", height=1)
    label.grid(row=4, column=3)

    button1 = Button(root, text=" ", font='roboto 25', bg="#CE9141", fg="#220047", height=4, width=8, command=lambda: btnClick(button1))
    button1.grid(row=3, column=0)

    button2 = Button(root, text=' ', font='roboto 25', bg="#CE9141", fg="#220047", height=4, width=8, command=lambda: btnClick(button2))
    button2.grid(row=3, column=1)

    button3 = Button(root, text=' ',font='roboto 25', bg="#CE9141", fg="#220047", height=4, width=8, command=lambda: btnClick(button3))
    button3.grid(row=3, column=2)

    button4 = Button(root, text=' ', font='roboto 25', bg="#CE9141", fg="#220047", height=4, width=8, command=lambda: btnClick(button4))
    button4.grid(row=4, column=0)

    button5 = Button(root, text=' ', font='roboto 25', bg="#CE9141", fg="#220047", height=4, width=8, command=lambda: btnClick(button5))
    button5.grid(row=4, column=1)

    button6 = Button(root, text=' ', font='roboto 25', bg="#CE9141", fg="#220047", height=4, width=8, command=lambda: btnClick(button6))
    button6.grid(row=4, column=2)

    button7 = Button(root, text=' ', font='roboto 25', bg="#CE9141", fg="#220047", height=4, width=8, command=lambda: btnClick(button7))
    button7.grid(row=5, column=0)

    button8 = Button(root, text=' ', font='roboto 25', bg="#CE9141", fg="#220047", height=4, width=8, command=lambda: btnClick(button8))
    button8.grid(row=5, column=1)

    button9 = Button(root, text=' ', font='roboto 25', bg="#CE9141", fg="#220047", height=4, width=8, command=lambda: btnClick(button9))
    button9.grid(row=5, column=2)
    
    disableButton()
    
    root.mainloop()
GUI()
