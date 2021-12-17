from tkinter import * 
from PIL import Image,ImageTk
from random import randint

#mainwindow

m = Tk()
m.title("Rock Paper Scissors")
m.config(bg = "purple")

# image 

image_r1 = ImageTk.PhotoImage(Image.open("rock 1.png"))
image_p1 = ImageTk.PhotoImage(Image.open("paper 1.png"))
image_s1 = ImageTk.PhotoImage(Image.open("scissors 1.png"))
image_r2 = ImageTk.PhotoImage(Image.open("rock 2.png"))
image_p2 = ImageTk.PhotoImage(Image.open("paper 2.png"))
image_s2 = ImageTk.PhotoImage(Image.open("scissors 2.png"))

#label

player_label = Label(m,image = image_r1)
comp_label = Label(m,image = image_r2)  
player_label.grid(row = 1,column = 0)
comp_label.grid(row = 1,column = 4)

#score

player_score = Label(m,text = 0, font = 4000 , bg = "white", fg = "black")
comp_score = Label(m,text = 0, font = 400 , bg = "white" , fg = "black")
player_score.grid(row = 1,column = 1)
comp_score.grid(row = 1,column = 3 )

# indicator

user_indicator = Label(m,font = 150, text = "USER", bg= "blue" , fg = "pink")
player_indicator = Label(m,font = 150, text = "COMPUTER", bg= "blue" , fg = "pink")
user_indicator.grid(row = 0,column = 0)
player_indicator.grid(row = 0,column = 4)


# message

message = Label(m, font = 60, bg = "orange", fg = "black")
message.grid(row = 0,column = 2)

def updateMessage(a):
    message['text'] = a

def comp_update():
    score = int(comp_score['text'])
    score+=1
    comp_score["text"] = str(score)

def player_update():
    score = int(player_score['text'])
    score+=1
    player_score["text"] = str(score)


# main

def winner(player,comp):
    if player == comp:
        updateMessage("It's a Tie")
    
    elif player == "Rock":
        if comp == "Paper":
            updateMessage("Computer Wins")
            comp_update()
        elif comp == "Scissors":
            updateMessage("Player Wins")
            player_update()
    
    elif player == "Paper":
        if comp == "Scissors":
            updateMessage("Computer Wins")
            comp_update()
        elif comp == "Rock":
            updateMessage("Player Wins")
            player_update()

    elif player == "Scissors":
        if comp == "Rock":
            updateMessage("Computer Wins")
            comp_update()
        elif comp == "Paper":
            updateMessage("Player Wins")
            player_update()

    else:
        pass


# make choice

select = ['Rock','Paper','Scissors']

def choice(x):
    comp_choice = select[randint(0,2)]
    if comp_choice == "Rock":
        comp_label.configure(image = image_r2)
    elif comp_choice == "Paper":
        comp_label.configure(image = image_p2)
    else:
        comp_label.configure(image = image_s2)

    if x == "Rock":
        player_label.configure(image = image_r1)
    elif x == "Paper":
        player_label.configure(image = image_p1)
    else:
        player_label.configure(image = image_s1)

    winner(x, comp_choice)


# Buttons

button_r = Button(m,width = 20, height = 2, text = "Rock", font = 15, bg = "black", fg = "white", command = lambda : choice("Rock"))
button_p = Button(m,width = 20, height = 2, text = "Paper", font = 15, bg = "black", fg = "white", command = lambda : choice("Paper"))
button_s = Button(m,width = 20, height = 2, text = "Scissors", font = 15, bg = "black", fg = "white", command = lambda : choice("Scissors"))
button_r.grid(row = 2,column = 1)
button_p.grid(row = 2,column = 2)
button_s.grid(row = 2,column = 3)


m.mainloop()
