from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

#Window:
window = Tk()
window.title("**Flashpoint**")
window.config(padx=50, bg=BACKGROUND_COLOR)



canvas = Canvas(height=700, width=800, bg=BACKGROUND_COLOR)
logo_image = PhotoImage(file="card_front.png")
canvas.create_image(400, 300, image=logo_image) #half of 200 is 100, so thats the center of the page
canvas.grid()









window.mainloop()