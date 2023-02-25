'''
Rashad Khan 
LAB 5 Module
Completed: 02/24/2023
ID:010713326
'''


import turtle
import random
turtle.colormode(255)

#function to draw a polygon with a given size
def draw_polygon(n, length):
    angle = 360 / n
    for i in range(n):
        turtle.speed('fastest')
        turtle.forward(length)
        turtle.left(angle)
    turtle.left((360/n)*2)

#keeps turtle page open
def keep_turtle():
    turtle.hideturtle()
    turtle.done()
    

#randomize pen color
def rand_pen_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turtle.color((r, g, b))

#setter functio for pen size
def set_pen_size(n):
    turtle.pensize(n)

#setter function for bg color
def set_bg(a):
    turtle.bgcolor(a)