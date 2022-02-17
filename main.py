# COde By Ritik Barnwal 
# BarnwalJitechnical.com
# Youtube : youtube.com/c/barnwaljitechnical

from cProfile import label
from email.mime import image
from tkinter import *
from PIL import Image, ImageTk
from random import randint

window = Tk()
window.title("Game Rock Paper Scissor")

# Size of window
window.geometry('1900x780')

# Creating canvas
window.configure(background="black", width=800, height=680)

# import the images 
image_rock1 = ImageTk.PhotoImage(Image.open("rock1.jpg"))
image_paper1 = ImageTk.PhotoImage(Image.open("paper1.jpg"))
image_scissor1 = ImageTk.PhotoImage(Image.open("scissor1.jpg"))
image_rock2 = ImageTk.PhotoImage(Image.open("rock.jpeg"))
image_paper2 = ImageTk.PhotoImage(Image.open("paper.jpeg"))
image_scissor2 = ImageTk.PhotoImage(Image.open("scissor.jpeg"))

# Default image
img_p = Image.open("default.jpeg")
img_p = img_p.resize((300, 300))


#Creating lables 
label_player = Label(window, image= image_scissor1)
label_computer = Label(window, image= image_scissor2)
l3 = Label(window, text='Vs', font=('Algerian', 40))

#placing the lables on window
label_computer.grid(row=1, column=0)
label_player.grid(row=1, column=4)
l3.grid(row=1, column=2)


# creating Score Board label 
computer_score = Label(window,text=0, font=('arial', 60, "bold"), fg="blue")
player_score = Label(window,text=0, font=('arial', 60, "bold"), fg="red")
computer_score.grid(row=1,column=1)
player_score.grid(row=1,column=3)

# player Indicator
player_indicator = Label(window, font=("arial", 40, "bold"),
                        text="PLAYER", bg="orange", fg="blue")
computer_indicator = Label(window, font=("arial", 40, "bold"),
                        text="COMPUTER", bg="orange", fg="blue")
computer_indicator.grid(row=0, column=1)
player_indicator.grid(row=0, column=3)


# making functions
def updateMessage (a):
    final_message['text'] = a

def Computer_Update():
    final = int(computer_score['text'])
    final += 1
    computer_score["text"] = str(final)

def Player_Update():
    final = int(player_score['text'])
    final += 1
    player_score["text"] = str(final)

# making winner checking function
def winner_check(p,c):
    if p == c:
        updateMessage("It's a tie")
    
    elif p == "rock":
        if c == "paper":
            updateMessage("Computer Wins !!")
            Computer_Update()
        else:
            updateMessage("Player Wins !!")
            Player_Update()
    
    elif p == "paper":
        if c == "scissor":
            updateMessage("Computer Wins !!")
            Computer_Update()
        else:
            updateMessage("Player Wins !!")
            Player_Update()

    
    elif p == "scissor":
        if c == "rock":
            updateMessage("Computer Wins !!")
            Computer_Update()
        else:
            updateMessage("Player Wins !!")
            Player_Update()
    else:
        pass

# define the rock paper scissor images for computer
to_select = ["rock", "paper", "scissor"]

def choice_update(a):

    choice_computer = to_select[randint(0,2)]
    if choice_computer == "rock":
        label_computer.configure(image=image_rock2)
    elif choice_computer == "paper":
        label_computer.configure(image= image_paper2)
    else:
        label_computer.configure(image= image_scissor2)

# define the rock paper scissor images for player
    if a == "rock":
        label_player.configure(image= image_rock1)
    elif a == "paper":
        label_player.configure(image= image_paper1)
    else:
        label_player.configure(image= image_scissor1)


    winner_check(a, choice_computer)



final_message = Label(window,font=("arial", 40, "bold"), bg="red", fg="white")
final_message.grid(row=3, column=2)



# creating Buttons
button_rock = Button(window,width=16, height=3, text="ROCK",
                    font=("arial", 20, "bold"), bg="yellow", fg="red", command=lambda:choice_update("rock")).grid(row=2,column=1)

button_paper = Button(window,width=16, height=3, text="PAPER",
                    font=("arial", 20, "bold"), bg="yellow", fg="red", command=lambda:choice_update("paper")).grid(row=2,column=2)

button_scissor = Button(window,width=16, height=3, text="SCISSOR",
                    font=("arial", 20, "bold"), bg="yellow", fg="red", command=lambda:choice_update("scissor")).grid(row=2,column=3)



window.mainloop()
