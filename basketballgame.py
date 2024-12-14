import turtle as trtl

#set up the screen
screen = trtl.Screen()
screen.bgcolor("gray")

#create the basketball 
ball = trtl.Turtle()
ball.shape('circle')

#initialize a list of colors
colors = ["orange", "red", "blue", "green"]

#ask the user to enter a color
user_input = input("What color do you want for the basketball? (options: orange, red, blue, green): ")

#set the basketball color based on user input, default to orange if invalid
if user_input in colors:
    ball.color(user_input)
else:
    ball.color("orange")  # default color

ball.speed(1)


#create the basketball hoop 
hoop = trtl.Turtle()
hoop.penup()
hoop.goto(120, 50)  
hoop.pendown()
hoop.circle(30)


#initialize the variables for the net of the hoop 
initial_angle = 270  
angle_step = 45   
num_lines = 8


#create loop to draw the net
for i in range(num_lines):
    hoop.penup()
    hoop.goto(120, 80)  
    hoop.pendown()
    hoop.color("white")
    
   #alternate between angles to make sure the lines of the net are symmetric
    if i % 2 == 0:  
        current_angle = initial_angle + (angle_step * (i // 2))
    else:  
        current_angle = initial_angle - (angle_step * ((i + 1) // 2))
    
    #set the direction of the next line
    hoop.setheading(current_angle) 
    hoop.forward(30)  


#create the stickman
stickman = trtl.Turtle()
stickman.speed(1)

#draw the head
stickman.penup()
stickman.goto(-50, 0)  
stickman.pendown()
stickman.circle(10)  

#draw the body
stickman.penup()
stickman.goto(-50, 0)
stickman.pendown()
stickman.goto(-50, -40) 

#draw the left arm
stickman.penup()
stickman.goto(-50, -10)
stickman.pendown()
stickman.goto(-70, -20)

#draw the right arm
stickman.penup()
stickman.goto(-50, -10)
stickman.pendown()
stickman.goto(-30, -5)

#draw the left leg
stickman.penup()
stickman.goto(-50, -40)
stickman.pendown()
stickman.goto(-60, -60)

#draw the right leg
stickman.penup()
stickman.goto(-50, -40)
stickman.pendown()
stickman.goto(-40, -60)

#move the ball and initialize the x-position and y-position of the ball
ball.penup()
x = -30  
y = -5   


#create loop to move ball toward th hoop
for step in range(10):
    #check to see if the ball is not too close to the hoop
    if ball.distance(200, 50) >= 30:  
        #move the ball to the tight
        x += 12
        if step < 10:
            #move the ball to the up during the first half movement 
            y += 10
        else:
            #move the ball down during the second half of movement
            y -= 10
        ball.goto(x, y)

#put ball in the center of hoop 
ball.goto(120,80)

trtl.done()




