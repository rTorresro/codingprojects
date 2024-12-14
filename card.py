import turtle as trtl
import random as rand


# set up the screen with background
screen = trtl.Screen()
screen.bgcolor("black")

# initial instruction turtle to display opening messtage
instruction_turtle = trtl.Turtle()
instruction_turtle.hideturtle()
instruction_turtle.color("white")
instruction_turtle.penup()
instruction_turtle.goto(0, 0)

# display the initial instruction message
instruction_turtle.write("Press enter to open the card", align="center", font=("Arial", 24, "bold"))


def show_instruction():
    instruction_turtle.clear()  

# initialize firework colors list and messages list
firework_colors = ["red", "yellow", "blue", "purple", "green", "orange"]
messages = [
    "Celebrate your wins, big and small!",
    "You’re lighting up the sky!",
    "Keep reaching new heights!",
    "Your future is bright!",
    "Let your light shine!"
]

# set up turtle for displaying the message
message_turtle = trtl.Turtle()
message_turtle.hideturtle()
message_turtle.penup()
message_turtle.color("white")
message_turtle.goto(0, 200)

# create display message function
def display_message():
    message_turtle.clear()
    message = rand.choice(messages)
    message_turtle.write(message, align="center", font=("Arial", 20, "bold"))

# create draw firework function
def draw_firework(x, y):
    firework = trtl.Turtle()
    firework.speed(0)
    firework.color(rand.choice(firework_colors))
    firework.penup()
    firework.goto(x, y)
    firework.hideturtle()
    if y > 0:
      firework_size = 70
    else:
      firework_size = 50
    for i in range(20):
        angle = rand.randint(0, 360)
        firework.setheading(angle)
        firework.forward(50)
        firework.dot(10)
        firework.goto(x, y)
    firework.hideturtle()

# create function for user input
def on_click(x, y):
    draw_firework(x, y)
    display_message()

screen.listen()
screen.onkey(show_instruction, "Return")
screen.onclick(on_click)
screen.mainloop()







