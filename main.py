from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"
card = {}

try:
    data = pd.read_csv('data/words_to_learn.csv')

except FileNotFoundError:
    data = pd.read_csv('data/french_words.csv')
    
finally:
    french_dic_to_learn = data.to_dict(orient="records")

# ---------------------------- FLIP THE CARD ------------------------------- # 

def flip_card():
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=card["English"], fill="white")

# ---------------------------- CREATE NEW FLASH CARD ------------------------------- # 

def card_known():
    french_dic_to_learn.remove(card)
    words_file = pd.DataFrame(french_dic_to_learn)
    words_file.to_csv("data/words_to_learn.csv", index=False)
    next_card()

    
def next_card():
    global card, flip_timer
    window.after_cancel(flip_timer)
    card = random.choice(french_dic_to_learn)
    canvas.itemconfig(card_title, text="French", fil="black")
    canvas.itemconfig(card_word, text=card["French"], fil="black")
    canvas.itemconfig(canvas_img, image=card_front_img)
    flip_timer = window.after(3000, flip_card)

# ---------------------------- UI SETUP ------------------------------- #

# Create the window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50)
window.config(bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

# Create the flash card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 264, image=card_front_img) 
card_title = canvas.create_text(400, 150, text="Title", fill="black", font=(FONT_NAME, 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", fill="black", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Create the buttons
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
right_button = Button(image=right_img, highlightthickness=0, command=card_known)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
right_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)


next_card()

window.mainloop()
