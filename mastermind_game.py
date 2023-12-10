import turtle as t
from Marble import Marble
from Point import Point
from random import shuffle
from os import path
from container import Container, GameDisplay, Leaderboard, UserBoard

class MastermindGame:
    def __init__(self):
        self.leaderboard_file = "leaderboard.txt"
        self.current_row = 0
        self.current_col = 0
        self.gameover = False
        self.ans_count = 1
        self.ans_limit = 10
        self.colors = ["blue", "red", "green", "yellow", "purple", "black"]
        self.display_colors = self.colors.copy()
        self.available_colors_per_row = [self.colors.copy() for _ in range(10)]
        self.shuffled_colors = self.colors.copy()
        shuffle(self.shuffled_colors)
        self.code = self.shuffled_colors[:4]
        self.guess_marbles = [[Marble(Point(-250 + col * 50, 210 - row * 50), "grey", 15) for col in range(4)] for row in range(10)]
        self.current_guess = []

    def get_player_name(self):
        return t.textinput("Player Name", "Enter your name:")

    def setup_color_picker(self):
        color_picker_turtle = t.Turtle()
        color_picker_turtle.penup()
        color_picker_turtle.hideturtle()
        color_picker_turtle.speed('fastest')

        start_x = -110
        start_y = -250
        for index, color in enumerate(self.colors):
            t.register_shape(color + "_circle", ((-10, -10), (-10, 10), (10, 10), (10, -10)))
            button = t.Turtle(shape=color + "_circle")
            button.color(color)
            button.penup()
            button.goto(start_x + index * 50, start_y)
            button.onclick(lambda x, y, color=color: self.on_color_selected(color))

    def on_color_selected(self, color):
        if len(self.current_guess) < 4 and color not in self.current_guess:
            self.current_guess.append(color)
            self.update_game_board()

    def update_game_board(self):
        for i, color in enumerate(self.current_guess):
            self.guess_marbles[self.current_row][i].set_color(color)
            self.guess_marbles[self.current_row][i].draw()

# Create an instance of the MastermindGame class
game = MastermindGame()

# Call the color picker setup method to display it
game.setup_color_picker()


# Add this line to register the check button image
t.addshape("checkbutton.gif")
t.addshape("xbutton.gif")  # Register the xbutton shape
t.addshape("quit.gif")
t.addshape("quitmsg.gif")
t.addshape("winner.gif")

# Create a Turtle for the check button
check_button = t.Turtle()
check_button.shape("checkbutton.gif")  # Ensure 'checkbutton.gif' is in the same directory
check_button.penup()
check_button.goto(0, -300)  # Adjust the position as needed

# Create a Turtle for the quit button
quit_button = t.Turtle()
quit_button.shape("quit.gif")
quit_button.penup()
quit_button.goto(250, -250)  # Adjust the position as needed

# Function to be called when quit button is clicked
def on_quit_click(x, y):
    # Show the quit message popup
    quitmsg_turtle = t.Turtle()
    quitmsg_turtle.shape("quitmsg.gif")  # Ensure 'quitmsg.gif' is in the same directory
    quitmsg_turtle.penup()
    quitmsg_turtle.goto(0, 0)  # Position the quit message popup
    # Here you can wait for a click to close the message and quit the game
    # or you can directly close the game window using wn.bye()

    # Bind the click event to the quit button
    quit_button.onclick(on_quit_click)

# Function to be called when check button is clicked
def on_check_click(x, y):
    # Check the player's guess
    # If the player's guess is correct, show the winner message
    winner_turtle = t.Turtle()
    winner_turtle.shape("winner.gif")  # Ensure 'winner.gif' is in the same directory
    winner_turtle.penup()
    winner_turtle.goto(0, 0)  # Position the winner message
    # Here you can wait for a click to close the message and quit the game
    # or you can directly close the game window using wn.bye()

    # Bind the click event to the quit button
    quit_button.onclick(on_quit_click)


screen = t.Screen()
screen.setup(width=600, height=800)
# Create and draw each section
game_display = GameDisplay()
leaderboard = Leaderboard()
userboard = UserBoard()
game_display.draw()
leaderboard.draw()
userboard.draw()
game_display.draw_marbles_and_indicators()  # Call to display marbles and indicators in GameDisplay
# Display the leaderboard
# Bind the click event to the check button
check_button.onclick(on_check_click)
# Bind the click event to the quit button
quit_button.onclick(on_quit_click)
t.listen()


def main(self):
        player_name = self.get_player_name()
        wn = t.Screen()
        wn.title("Mastermind")
        wn.bgcolor("white")
        wn.setup(width=600, height=800)

        self.setup_game_screen()
        self.setup_color_picker()

        if not path.exists(self.leaderboard_file):
            open(self.leaderboard_file, "x").close()

t.listen()
t.mainloop()