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

#Labels:
# title_label = Label()
# title_label.config(text="Title")
# title_label.grid(row=0, column=1)
#
# word_label = Label()
# word_label.config(text="Word")
# word_label.grid(row=1, column=1)
#
# #Buttons:
right_button = Button()
right_button.config(text="Right")
right_button.grid(row=1, column=0)

wrong_button = Button()
wrong_button.config(text="Wrong")
wrong_button.grid(row=1, column=1)
#
#






window.mainloop()