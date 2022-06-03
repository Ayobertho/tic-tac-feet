from tkinter import *
from tkinter import messagebox

root = Tk()
#root.geometry('385x400')
root.title('TicTacToe')

click = True
count = 0

def reset():
	pass

def helpMe():
	pass

def disable_all_buttons():
	b1.config(state=DISABLED)
	b2.config(state=DISABLED)
	b3.config(state=DISABLED)
	b4.config(state=DISABLED)
	b5.config(state=DISABLED)
	b6.config(state=DISABLED)
	b7.config(state=DISABLED)
	b8.config(state=DISABLED)
	b9.config(state=DISABLED)


def checkWinner():
	global winner
	winner = False

	#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
	if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
		winner = True
		b1.config(bg='green')
		b2.config(bg='green')
		b3.config(bg='green')
		messagebox.showinfo('TicTacToe','X is a Winner!')
		disable_all_buttons()
	elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
		winner = True
		b1.config(bg='green')
		b5.config(bg='green')
		b9.config(bg='green')
		messagebox.showinfo('TicTacToe','X is a Winner!')
		disable_all_buttons()
	elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
		winner = True
		b1.config(bg='green')
		b4.config(bg='green')
		b7.config(bg='green')
		messagebox.showinfo('TicTacToe','X is a Winner!')
		disable_all_buttons()
	elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
		winner = True
		b4.config(bg='green')
		b5.config(bg='green')
		b6.config(bg='green')
		messagebox.showinfo('TicTacToe','X is a Winner!')
		disable_all_buttons()
	elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
		winner = True
		b7.config(bg='green')
		b8.config(bg='green')
		b9.config(bg='green')
		messagebox.showinfo('TicTacToe','X is a Winner!')
		disable_all_buttons()
	elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
		winner = True
		b3.config(bg='green')
		b5.config(bg='green')
		b7.config(bg='green')
		messagebox.showinfo('TicTacToe','X is a Winner!')
		disable_all_buttons()
	elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
		winner = True
		b3.config(bg='green')
		b6.config(bg='green')
		b9.config(bg='green')
		messagebox.showinfo('TicTacToe','X is a Winner!')
		disable_all_buttons()
	elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
		winner = True
		b2.config(bg='green')
		b5.config(bg='green')
		b8.config(bg='green')
		messagebox.showinfo('TicTacToe','X is a Winner!')
		disable_all_buttons()
	# OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
	if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
		winner = True
		b1.config(bg='green')
		b2.config(bg='green')
		b3.config(bg='green')
		messagebox.showinfo('TicTacToe','O is a Winner!')
		disable_all_buttons()
	elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
		winner = True
		b1.config(bg='green')
		b5.config(bg='green')
		b9.config(bg='green')
		messagebox.showinfo('TicTacToe','O is a Winner!')
		disable_all_buttons()
	elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
		winner = True
		b1.config(bg='green')
		b4.config(bg='green')
		b7.config(bg='green')
		messagebox.showinfo('TicTacToe','O is a Winner!')
		disable_all_buttons()
	elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
		winner = True
		b4.config(bg='green')
		b5.config(bg='green')
		b6.config(bg='green')
		messagebox.showinfo('TicTacToe','O is a Winner!')
		disable_all_buttons()
	elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
		winner = True
		b7.config(bg='green')
		b8.config(bg='green')
		b9.config(bg='green')
		messagebox.showinfo('TicTacToe','O is a Winner!')
		disable_all_buttons()
	elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
		winner = True
		b3.config(bg='green')
		b5.config(bg='green')
		b7.config(bg='green')
		messagebox.showinfo('TicTacToe','O is a Winner!')
		disable_all_buttons()
	elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
		winner = True
		b3.config(bg='green')
		b6.config(bg='green')
		b9.config(bg='green')
		messagebox.showinfo('TicTacToe','O is a Winner!')
		disable_all_buttons()
	elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
		winner = True
		b2.config(bg='green')
		b5.config(bg='green')
		b8.config(bg='green')
		messagebox.showinfo('TicTacToe','O is a Winner!')
		disable_all_buttons()

def point(pointer):
	global click, count

	if pointer["text"] == " " and click == True:
		pointer["text"] = "X"
		click = False
		count = count + 1
		checkWinner()
	elif pointer["text"] == " " and click == False:
		pointer["text"] = "O"
		click = True
		count = count + 1
		checkWinner()
	else:
		messagebox.showerror('TicTacToe','Please click another box!')
	if count == 9 and winner == False:
		messagebox.showinfo('TicTacToe','Tie!')

b1 = Button(root,text=' ',height=3,width=6,font=('Arial',14),command = lambda: point(b1))
b2 = Button(root,text=' ',font=('Arial',14),height=3,width=6,command = lambda: point(b2))
b3 = Button(root,text=' ',font=('Arial',14),height=3,width=6,command = lambda: point(b3))

b4 = Button(root,text=' ',font=('Arial',14),height=3,width=6,command = lambda: point(b4))
b5 = Button(root,text=' ',font=('Arial',14),height=3,width=6,command = lambda: point(b5))
b6 = Button(root,text=' ',font=('Arial',14),height=3,width=6,command = lambda: point(b6))

b7 = Button(root,text=' ',font=('Arial',14),height=3,width=6,command = lambda: point(b7))
b8 = Button(root,text=' ',font=('Arial',14),height=3,width=6,command = lambda: point(b8))
b9 = Button(root,text=' ',font=('Arial',14),height=3,width=6,command = lambda: point(b9))

b1.grid(column=1,row=2)
b2.grid(column=2,row=2)
b3.grid(column=3,row=2)

b4.grid(column=1,row=3)
b5.grid(column=2,row=3)
b6.grid(column=3,row=3)

b7.grid(column=1,row=4)
b8.grid(column=2,row=4)
b9.grid(column=3,row=4)

def reset():
	#reset 

	global b1,b2,b3,b4,b5,b6,b7,b8,b9
	global click,count
	click = True
	count = 0

	b1 = Button(root,text=' ',font=('Arial',14),height=3,width=6,command = lambda: point(b1))
	b2 = Button(root,text=' ',font=('Arial',14),height=3,width=6,command = lambda: point(b2))
	b3 = Button(root,text=' ',font=('Arial',14),height=3,width=6,command = lambda: point(b3))

	b4 = Button(root,text=' ',font=('Arial',14),height=3,width=6,command = lambda: point(b4))
	b5 = Button(root,text=' ',font=('Arial',14),height=3,width=6,command = lambda: point(b5))
	b6 = Button(root,text=' ',font=('Arial',14),height=3,width=6,command = lambda: point(b6))

	b7 = Button(root,text=' ',font=('Arial',14),height=3,width=6,command = lambda: point(b7))
	b8 = Button(root,text=' ',font=('Arial',14),height=3,width=6,command = lambda: point(b8))
	b9 = Button(root,text=' ',font=('Arial',14),height=3,width=6,command = lambda: point(b9))

	b1.grid(column=1,row=2)
	b2.grid(column=2,row=2)
	b3.grid(column=3,row=2)

	b4.grid(column=1,row=3)
	b5.grid(column=2,row=3)
	b6.grid(column=3,row=3)

	b7.grid(column=1,row=4)
	b8.grid(column=2,row=4)
	b9.grid(column=3,row=4)

def helpMe():
	messagebox.showinfo('TicTacToe','If become Three X or O with side by side or Cross, It be a winner!')

# MENU
my_menu = Menu(root)
root.config(menu=my_menu)

options_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label='Options', menu=options_menu)
options_menu.add_command(label='Reset Game',command=reset)

help_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='Help..',command=helpMe)

reset()

root.mainloop()