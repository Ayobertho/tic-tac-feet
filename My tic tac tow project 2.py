
from tkinter import * 
from tkinter import messagebox
root = Tk()
root.title("Robbie's tic tac toe :)")
root.resizable(False, False)
#root.geometry("350x350")

# X starts so True
clicked = True
count = 0 


def reset():
	pass

def helpMe():
	pass


# to clear the buttons of O and X
def disable_all_buttons():
    b1.config( state = DISABLED)
    b2.config( state = DISABLED)
    b3.config( state = DISABLED)
    b4.config( state = DISABLED)
    b5.config( state = DISABLED)
    b6.config( state = DISABLED)
    b7.config( state = DISABLED)
    b8.config( state = DISABLED)
    b9.config( state = DISABLED)
    
def checkWinner():
	global winner
	winner = False

# X'S WINNING POSSIBILITIES 
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
# O's WINNING POSIBILITES
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

#button clicked function
def b_click(b):
    global clicked, count
    if  b["text"] == " " and clicked == True:
        b["text"] == "X" 
        clicked = False 
        count = count + 1 
        checkWinner()
    elif b["text"] == " " and clicked == False:
         b["text"] == "0" 
         clicked = True
         count = count + 1
         checkWinner()
    else:
        messagebox.showerror("Tic Tac Toe", "Hey that box is already been selected\nPick Another Box..")


	

#build our buttons
b1 = Button(root, text=" ", font=("Arial", 20), height=3, width=6, command=lambda: b_click(b1))
b2 = Button(root, text=" ", font=("Arial", 20), height=3, width=6,  command=lambda: b_click(b2))
b3 = Button(root, text=" ", font=("Arial", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))

b4 = Button(root, text=" ", font=("Arial", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
b5 = Button(root, text=" ", font=("Arial", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
b6 = Button(root, text=" ", font=("Arial", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))

b7 = Button(root, text=" ", font=("Arial", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
b8 = Button(root, text=" ", font=("Arial", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
b9 = Button(root, text=" ", font=("Arial", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))


#Grid our buttons to the screen
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)



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









