from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"


data_frame = pandas.read_csv("spanish_words.csv")
# print(type(data_frame)) #prints dataframe
# print(data_frame)
to_learn = data_frame.to_dict(orient="records") #Changed the orient **
print(to_learn) #prints a list consisting od dicts **
print(type(to_learn)) #prints: list


def next_card():
    current_card = random.choice(to_learn) #lets say it picks 8th entry in list which is: {'Spanish': 'que', 'English': 'that'}
    print(current_card["Spanish"]) #the current_card["Spanish"] = "que", and current_card["English"] = "that"
    canvas.itemconfig(card_title, text="Spanish")
    canvas.itemconfig(card_word, text=current_card["Spanish"])




#Window:
window = Tk()
window.title("**Flashpoint**")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


#Canvas
canvas = Canvas(height=600, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="card_front.png")
canvas.create_image(410, 300, image=card_front_image)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(380, 200, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(380, 320, text="Word", font=("Arial", 40, "italic"))



#Buttons:
check_image = PhotoImage(file="right.png")
unknown_button = Button(image=check_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

cross_image = PhotoImage(file="wrong.png")
known_button = Button(image=cross_image, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)

#
# next_card()



window.mainloop()