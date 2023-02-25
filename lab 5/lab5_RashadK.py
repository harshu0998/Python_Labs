'''
Rashad Khan 
LAB 4
Completed: 02/19/2023
ID:010713326
'''


import draw_polygon

#set initial turtle value
draw_polygon.set_pen_size(1)
draw_polygon.set_bg('black')

#ask user for input
def input_from_person():
    number =int(input("please input a number : "))
    sides = int(input("please input a the number of sides for the generated shape : "))
    #gets an even number for making same amount of shapes for each section
    number = (sides*(number//sides))
    return number,sides

number, sides = input_from_person()

#find random color to start design
draw_polygon.rand_pen_color()

#make half the shapes so that center looks hollow (for artistic purposes)
for i in range((number//2),number):
    #change pen color at an apropriate frequency depending on shape
    if i%(sides) == 0:
        draw_polygon.rand_pen_color()
    draw_polygon.draw_polygon(sides,i)
#keep turtle
draw_polygon.keep_turtle()



