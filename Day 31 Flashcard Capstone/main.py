from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
RIGHT_BUTTON_PATH = "./images/right.png"
WRONG_BUTTON_PATH = "./images/wrong.png"
CARD_BACK_PATH = "./images/card_back.png"
CARD_FRONT_PATH = "./images/card_front.png"
WORDS_PATH = "./data/french_words.csv"
NEW_WORDS_PATH = "./data/words_to_learn.csv"
FONT = "Arial"
timer = None
word = None

window = Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# PANDAS
try:
    data = pandas.read_csv(NEW_WORDS_PATH)
except FileNotFoundError:
    data = pandas.read_csv(WORDS_PATH)
finally:
    languages = pandas.read_csv(WORDS_PATH, nrows=0).columns.tolist()
    word_dict = data.to_dict(orient="records")

# FUNCTIONS
def get_new_word():
    global timer, word
    if timer is not None:
        window.after_cancel(timer)
    word = choice(word_dict)
    canvas.itemconfig(card, image=card_front)
    canvas.itemconfig(language_txt, text=languages[0], fill="black")
    canvas.itemconfig(word_txt, text=word[languages[0]], fill="black")
    timer = window.after(3000, card_flip)


def card_flip():
    global word
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(language_txt, text=languages[1], fill="white")
    canvas.itemconfig(word_txt, text=word[languages[1]], fill="white")


def update_knowledge():
    global word
    word_dict.remove(word)
    new_data = pandas.DataFrame(word_dict)
    new_data.to_csv(NEW_WORDS_PATH, index=False)
    get_new_word()

# CANVAS
canvas = Canvas(width=800, height=570, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file=CARD_FRONT_PATH)
card_back = PhotoImage(file=CARD_BACK_PATH)
card = canvas.create_image(400, 263, image=card_front)
language_txt = canvas.create_text(400, 150, text="French", font=(FONT, 40, "italic"))
word_txt = canvas.create_text(400, 263, text="Placeholder", font=(FONT, 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

# BUTTONS
correct_button_img = PhotoImage(file=RIGHT_BUTTON_PATH)
correct_button = Button(image=correct_button_img, highlightthickness=0, command=update_knowledge)
correct_button.grid(row=1, column=1)

wrong_button_img = PhotoImage(file=WRONG_BUTTON_PATH)
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=get_new_word)
wrong_button.grid(row=1, column=0)

get_new_word()

window.mainloop()