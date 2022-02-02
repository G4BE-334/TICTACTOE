from tkinter import *
from tkinter import messagebox
import tkinter as tk
"""
Creation of a TicTacToe Game
Initiate the window
"""
win=Tk()
win.title("Tic Tac Toe")

bclick = True

mainFrm = Frame(win)
mainFrm.pack()


# Defining buttons
def ttt(buttons):
    global bclick
    if buttons["text"] == " " and bclick == True:
        buttons["fg"] = "red"
        buttons["text"] = "X"
        bclick = False
    elif buttons["text"] == " " and bclick == False:
        buttons['fg'] = "blue"
        buttons["text"] = "O"
        bclick = True
    CheckWinner()

# Clear board function
def clearBoard():
    button1["text"] = " "
    button2["text"] = " "
    button3["text"] = " "
    button4["text"] = " "
    button5["text"] = " "
    button6["text"] = " "
    button7["text"] = " "
    button8["text"] = " "
    button9["text"] = " "
    bclick = True

# Checking for winner
def CheckWinner():
    if(button1['text'] == button2['text'] == button3['text'] != ' ' or
    button4['text'] == button5['text'] == button6['text'] != ' ' or
    button7['text'] == button8['text'] == button9['text'] != ' ' or
    button1['text'] == button5['text'] == button9['text'] != ' ' or
    button3['text'] == button5['text'] == button7['text'] != ' ' or
    button1['text'] == button2['text'] == button3['text'] != ' ' or
    button1['text'] == button4['text'] == button7['text'] != ' ' or
    button2['text'] == button5['text'] == button8['text'] != ' ' or
    button3['text'] == button6['text'] == button9['text'] != ' ' or
    button7['text'] == button8['text'] == button9['text'] != ' '):
        if bclick:
            messagebox.showinfo("Player O",'Winner is O !')
        else:
            messagebox.showinfo("Player X",'Winner is X !')
        clearBoard()
    elif(button1['text'] != ' ' and button2['text'] != ' ' and button3['text'] != ' ' and
    button4['text'] != ' ' and button5['text'] != ' ' and button6['text'] != ' ' and
    button7['text'] != ' ' and button8['text'] != ' ' and button9['text'] != ' '):
        messagebox.showinfo("No winners","That's a tie!")
        clearBoard()



# Buttons and the colors to change
buttons=StringVar()

# Creation of buttons to represent the houses of TicTacToe
# Buttons from 1-9 starting on the top left
# Bottom right represent the last button
button1 = Button(mainFrm,text=" ",font=('Times 24 bold'),bg='gray',fg='blue',height=4,width=8,command=lambda:ttt(button1))
button1.grid(row=1,column=0,sticky = S+N+E+W)

button2 = Button(mainFrm,text=' ',font=('Times 24 bold'),bg='gray',fg='blue',height=4,width=8,command=lambda:ttt(button2))
button2.grid(row=1,column=1,sticky = S+N+E+W)

button3 = Button(mainFrm,text=' ',font=('Times 24 bold'),bg='gray',fg='blue',height=4,width=8,command=lambda:ttt(button3))
button3.grid(row=1,column=2,sticky = S+N+E+W)

button4 = Button(mainFrm,text=' ',font=('Times 24 bold'),bg='gray',fg='blue',height=4,width=8,command=lambda:ttt(button4))
button4.grid(row=2,column=0,sticky = S+N+E+W)

button5 = Button(mainFrm, text=' ',font=('Times 24 bold'),bg='gray',fg='blue',height=4,width=8,command=lambda:ttt(button5))
button5.grid(row=2,column=1,sticky = S+N+E+W)

button6 = Button(mainFrm,text=' ',font=('Times 24 bold'),bg='gray',fg='blue',height=4,width=8,command=lambda:ttt(button6))
button6.grid(row=2,column=2,sticky = S+N+E+W)

button7 = Button(mainFrm,text=' ',font=('Times 24 bold'),bg='gray',fg='blue',height=4,width=8,command=lambda:ttt(button7))
button7.grid(row=3,column=0,sticky = S+N+E+W)

button8 = Button(mainFrm,text=' ',font=('Times 24 bold'),bg='gray',fg='blue',height=4,width=8,command=lambda:ttt(button8))
button8.grid(row=3,column=1,sticky = S+N+E+W)

button9 = Button(mainFrm,text=' ',font=('Times 24 bold'),bg='gray',fg='blue',height=4,width=8,command=lambda:ttt(button9))
button9.grid(row=3,column=2,sticky = S+N+E+W)
win.mainloop()


