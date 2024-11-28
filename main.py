from turtle import Turtle, Screen
# Creating objects and initializing the class with the object
ani = Turtle()
screen = Screen()
ani.speed("fast")

# making the object move forward
def move_forwards():
    ani.forward(10)
    
# making the object to turn left by using the current position and adding 10 paces to it
def turn_left():
    new_heading = ani.heading() + 10
    ani.setheading(new_heading)
    
# making the object to turn right by using the current position and subtracting 10 paces to it
def turn_right():
    new_heading = ani.heading() - 10
    ani.setheading(new_heading)
    
# making the object move backward
def move_backwards():
    ani.backward(10)
    
# making the object to clear the sketch left behind and moving back to the initial position
def clear_screen():
    ani.clear()
    ani.penup()
    ani.home()
    ani.pendown()

# Calling all the functions and assigning them to the Up, Left,Right,Down movement.
screen.listen()
screen.onkey(key="Up", fun=move_forwards)
screen.onkey(key="Left",fun=turn_left)
screen.onkey(key="Right",fun=turn_right)
screen.onkey(key="Down",fun=move_backwards)
screen.onkey(key="c",fun=clear_screen)

screen.exitonclick()
