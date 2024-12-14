import turtle as trtl
import random as rand
import time

# set up obstacles list and font color
spot_color = "green"
obstacle_colors = ["red", "yellow", "purple", "blue", "orange"]
# initialize score 
score = 0
font_setup = ("Arial", 20, "normal")

# set up the screen
wn = trtl.Screen()
wn.title("Turtle Dodger")
wn.bgcolor("gray")
wn.setup(width=600, height=600)

# set up the turtle as the player and position the player 
player = trtl.Turtle()
player.shape("turtle")
player.color(spot_color)
player.penup()
player.goto(0, -250)  

# create scoreboard turtle and set up the scoreboard 
score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(0, 260)  # Position at the top of the screen
score_writer.write("Score: " + str(score), align="center", font=font_setup)
# Obstacles List
obstacles = []


# function to update scoreboard 
def update_score():
  
    global score
    score += 1
    score_writer.clear()
    score_writer.write("Score: " + str(score), align="center", font=font_setup)


# function for obstacles 
def create_obstacle():
    obstacle = trtl.Turtle()
    obstacle.shape("square")
    obstacle.color(rand.choice(obstacle_colors))
    obstacle.shapesize(stretch_wid=2, stretch_len=3)
    obstacle.penup()
    obstacle.goto(rand.randint(-280, 280), 300)  
    obstacles.append(obstacle)

# functions to move right and left 
def move_left():
    x = player.xcor()
    if x > -280:
        player.setx(x - 20)

def move_right():
    x = player.xcor()
    if x < 280:
        player.setx(x + 20)

# keyboard bindings
wn.listen()
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")

# main game loop
game_over = False
while not game_over:
    wn.update()
    # game speed control 
    time.sleep(0.02)  

    # periodically create new obstacles
    if rand.randint(1, 10) == 1:
        create_obstacle()

    # move obstacles and check for collision
    for obstacle in obstacles:
        obstacle.sety(obstacle.ycor() - 5)

        # reset position if obstacle goes off screen
        if obstacle.ycor() < -300:
            obstacle.hideturtle()
            obstacles.remove(obstacle)
            update_score()  

        # check for collision with player
        if player.distance(obstacle) < 20:
            game_over = True
            score_writer.clear()
            score_writer.write("Game Over!", align="center", font=("Arial", 36, "bold"))

wn.mainloop()


