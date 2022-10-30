import turtle
from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("words_to_learn")
except FileNotFoundError:
    original_data = pandas.read_csv("spanish_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")






def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn) #lets say it picks 8th entry in list which is: {'Spanish': 'que', 'English': 'that'}
    print(current_card["Spanish"]) #the current_card["Spanish"] = "que", and current_card["English"] = "that"
    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_word, text=current_card["Spanish"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, flip_card)
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white") #changes fill color
    canvas.itemconfig(card_word, text=current_card["English"], fill="white") #changes fill color
    canvas.itemconfig(card_background, image=card_back_image)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))

    #creates a list of storage of words i still need to learn
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn", index=False) #pandas does not add the index numbers to our newly created list **

    next_card()



#Window:
window = Tk()
window.title("**Flashpoint**")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)


#Canvas
canvas = Canvas(height=600, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="card_front.png")
card_back_image = PhotoImage(file="card_back.png")
card_background = canvas.create_image(410, 300, image=card_front_image)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(380, 200, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(380, 320, text="Word", font=("Arial", 40, "bold"))



#Buttons:
check_image = PhotoImage(file="right.png")
unknown_button = Button(image=check_image, highlightthickness=0, command=is_known)
unknown_button.grid(row=1, column=0)

cross_image = PhotoImage(file="wrong.png")
known_button = Button(image=cross_image, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)


next_card()



window.mainloop()