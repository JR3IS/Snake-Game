# SNAKE 

import turtle
import time
import random

delay = 0.1

score = 0
high_score = 0

segments = []

# Read high score from file
try:
    with open("highscore.txt", "r") as file:
        high_score = int(file.read())
except FileNotFoundError:
    high_score = 0

# Set up the screen 

win = turtle.Screen()
win.title("SNAKE")
win.bgcolor("black")
win.setup(width=600,height=600)
win.tracer(0) # Turns off the screen updates

# Snake Head

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("darkgreen")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Food

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("white")
food.penup()
food.goto(0,100)

# Pen 

pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(f"Score: {score} High Score: {high_score}", align='center',font=('courier', 15, 'normal'))

# Functions

def move() :
    
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
        
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
        
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
        
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

def go_up() :
    if head.direction != "down":
        head.direction = "up"
    
def go_down() :
    if head.direction != "up":
        head.direction = "down"

def go_left() :
    if head.direction != "right":
        head.direction = "left"
    
def go_right() :
    if head.direction != "left":
        head.direction = "right"

# Keyboard bindings

win.listen()
win.onkeypress(go_up, "w")
win.onkeypress(go_down, "s")
win.onkeypress(go_left, "a")
win.onkeypress(go_right, "d")

# Main game loop

while True:
    
    win.update()
    
    # Check for collision with the border
    
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290 :
        time.sleep(0.5)
        head.goto(0,0)
        head.direction="stop"
        
        # Hide the segments
        for segment in segments :
            segment.goto(1000,1000)
        
        # Clear the segments list
        segments = []
        
        # Reset the score
        score = 0
        pen.clear()
        pen.write(f'Score: {score}  High Score: {high_score}', align='center',font=('courier', 15, 'normal'))
        
        # Reset the delay
        delay=0.1
    
    # Check for collision with the food
    
    if head.distance(food) < 20:
        # Move food to random place
        x = random.randint(-270,270)
        y = random.randint(-270,270)
        food.goto(x ,y )
        
        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("darkgreen")
        new_segment.penup()
        segments.append(new_segment)
        
        # Increase the score
        score += 10
        
        if score > high_score :
            high_score = score
            
        # Save high score to file
            with open("highscore.txt", "w") as file:
                file.write(str(high_score))

        # Update the scoreboard    
        pen.clear()
        pen.write(f'Score: {score}  High Score: {high_score}', align='center',font=('courier', 15, 'normal'))
        
        # Shorten the delay
        delay -= 0.001
        
    # Move the end segments first in reverse order
    for index in range(len(segments)-1,0,-1) :
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)   
    
    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
        
    move()
    
    # Check for body collisions     
    for segment in segments: 
        if segment.distance(head)<20:
            time.sleep(0.5)
            head.goto(0,0)
            head.direction="stop"
            
            # Hide segments
            for segment in segments :
                segment.goto(1000,1000)
            
            # Clear segment list
            segments = []
            
            # Reset the score
            score=0
            pen.clear()
            pen.write(f'Score: {score}  High Score: {high_score}', align='center',font=('courier', 15, 'normal'))
            
            # Reset the delay
            delay=0.1
        
    
 
    time.sleep(delay)



win.mainloop()