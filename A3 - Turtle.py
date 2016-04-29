def clear_window():
    #Clears the entire window and sends the turtle back to his original origin#
    t.home()
    t.penup()
    t.clearscreen()
    return

def red_square():
    #Draws a red square (No Loop)
    #Non-productive function (Non values are returned)
    t.pencolor("red")
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    return

def blue_square():
    #Using for loop to draw a blue square
    #Non-productive function (No values are returned)
    t.pencolor("blue")
    for k in range(4):
        t.forward(100)
        t.left(90)
    return

def snowman_arms ():
    for i in range(40):
        t.fd(1)
        t.right(.2)
    return

def circle(radius, penwidth):
    #Two parameters
    t.width(penwidth)
    t.circle(radius)
    return

def two_semi_circle_color(radius, pencolor1 , fillcolor1, pencolor2, fillcolor2):
    #Draws two semicircle connected to each other with different fill color and pen color
    #Non-productive function
    #Receives five parameters: Radius, Pencolor 1, Fillcolor 1, Pencolor 2 & fillcolor2
    t.pencolor(pencolor1)
    t.fillcolor(fillcolor1)
    t.begin_fill()
    t.circle(radius,180)
    t.end_fill()
    t.pencolor(pencolor2)
    t.fillcolor(fillcolor2)
    t.begin_fill()
    t.circle(radius,180)
    t.end_fill()
    return

def random_speed():
    #returns a speed (from 1 to 10, faster as the value increase)
    fast = random.randint(1,10)
    t.speed(fast)
    return


    
## TOP LEVEL

import turtle as t
import random


t.speed(9)
two_semi_circle_color(90,"black","red","red","grey")
t.penup()
t.circle(90,180)
t.pendown()
t.speed(9)
snowman_arms()
t.right(180)
snowman_arms()
t.right(190)
t.heading()
snowman_arms

'''
# Drawing multiple squares #no loops function

t.left(30)
red_square()
t.left(800)
red_square()
t.left(100)
red_square()
t.right(260)
red_square()

# Clear space

clear_window()

# Drawing multiple squares #w/ loop function #Up and down
blue_square()
t.penup()
t.left(90)
blue_square()
t.pendown()
t.right(90)
blue_square()
t.backward(100)
blue_square()
t.penup()
t.forward(100)
t.pendown()
blue_square()

# Clear Space

clear_window()

# Two Semi Circles Filled with some color and changes pen
two_semi_circle_color(120,"red","green","yellow","blue")
t.left(180)
two_semi_circle_color(180,"black","red","red","grey")
snowman_arms()
t.right(125)
snowman_arms()
'''









    


    


