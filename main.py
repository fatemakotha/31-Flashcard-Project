from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"


data_frame = pandas.read_csv("spanish_words.csv")
# print(type(data_frame)) #prints dataframe
# print(data_frame)
to_learn = data_frame.to_dict(orient="records") #Changed the orient **
print(to_learn)


def next_card():
    pass



#Window:
window = Tk()
window.title("**Flashpoint**")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


#Canvas
canvas = Canvas(height=600, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="card_front.png")
canvas.create_image(410, 300, image=card_front_image)
canvas.grid(row=0, column=0, columnspan=2)
canvas.create_text(380, 200, text="Title", font=("Arial", 40, "italic"))
canvas.create_text(380, 320, text="Word", font=("Arial", 40, "italic"))



#Buttons:
check_image = PhotoImage(file="right.png")
unknown_button = Button(image=check_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

cross_image = PhotoImage(file="wrong.png")
known_button = Button(image=cross_image, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)






window.mainloop()