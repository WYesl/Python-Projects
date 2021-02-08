import pandas
import turtle

TOTAL_STATES = 50
states_done = 0

states_csv = pandas.read_csv("50_states.csv")
states = states_csv.state.to_list()
# print(states)

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

write_turtle = turtle.Turtle()
write_turtle.penup()
write_turtle.hideturtle()
write_turtle.speed("fastest")

already_guessed = []

game_on = True

while states_done < TOTAL_STATES and game_on:
    answer_state = screen.textinput(title=f"Guess the state({states_done}/{TOTAL_STATES})", prompt="What's another state's name?")
    if answer_state is not None:
        answer_state = answer_state.lower()
        answer_state = answer_state.capitalize()
    else:
        game_on = False
    if answer_state in states and answer_state not in already_guessed:
        states_done += 1
        already_guessed.append(answer_state)
        guessed_state = states_csv[states_csv.state == answer_state]

        write_turtle.goto(int(guessed_state.x), int(guessed_state.y))
        write_turtle.write(answer_state, False, "center")





turtle.mainloop()

unknown_states = [state for state in states if state not in already_guessed]

states_to_learn = {
    "states": unknown_states
}

new_data = pandas.DataFrame(states_to_learn)
new_data.to_csv("states_to_learn.csv")