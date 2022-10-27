from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

#Window:
window = Tk()
window.title("**Flashpoint**")



canvas = Canvas(height=600, width=800)
logo_image = PhotoImage(file="card_front.png")
canvas.create_image(400, 300, image=logo_image) #half of 200 is 100, so thats the center of the page
canvas.grid()









window.mainloop()