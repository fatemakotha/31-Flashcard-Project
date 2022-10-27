from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

#Window:
window = Tk()
window.title("**Flashpoint**")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


#Canvas
canvas = Canvas(height=700, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
logo_image = PhotoImage(file="card_front.png")
canvas.create_image(400, 300, image=logo_image) #half of 200 is 100, so thats the center of the page
canvas.grid(row=0, column=0, columnspan=2)

# Labels:
title_label = Label()
title_label.config(text="Title", font=("Arial", 40, "italic"))
title_label.place(x=340, y=150)

word_label = Label()
word_label.config(text="Word", font=("Arial", 40, "bold"))
word_label.place(x=330, y=300)


# #Buttons:

right_image = PhotoImage(file="right.png")
right_button = Button(image=right_image)
right_button.grid(row=1, column=0)

wrong_image = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_image)
wrong_button.grid(row=1, column=1)






window.mainloop()