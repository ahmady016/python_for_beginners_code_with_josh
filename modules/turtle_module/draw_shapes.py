from turtle import Turtle, exitonclick
###################################################################
def draw_shape(sides, size, color, thickness=1, position=(0, 0)):
    # create a turtle object
    t = Turtle()
    # up the pen and move to the position and down the pen again to draw
    t.penup()
    t.goto(position)
    t.pendown()
    # set the color and thickness
    t.color(color)
    t.pensize(thickness)
    # draw the shape using each side and fill it
    t.begin_fill()
    for i in range(sides):
        t.forward(size)
        t.left(360 / sides)
    t.end_fill()
###################################################################
def draw_circle(radius, color, thickness=1, position=(0, 0)):
    t = Turtle()
    # up the pen and move to the position and down the pen again to draw
    t.penup()
    t.goto(position)
    t.pendown()
    # set the color and thickness
    t.color(color)
    t.pensize(thickness)
    # draw the circle and fill it
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
###################################################################
def draw_star(width, color, size=50, thickness=1, position=(0, 0)):
    t = Turtle()
    # up the pen and move to the position and down the pen again to draw
    t.penup()
    t.goto(position)
    t.pendown()
    # set the color and thickness
    t.width(width)
    t.color(color)
    t.pensize(thickness)
    # draw the star and fill it
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.left(144)
    t.end_fill()
###################################################################
def draw_rectangle(width, height, color, thickness=1, position=(0, 0)):
    t = Turtle()
    # up the pen and move to the position and down the pen again to draw
    t.penup()
    t.goto(position)
    t.pendown()
    # set the color and thickness
    t.color(color)
    t.pensize(thickness)
    # draw the oval and fill it
    t.begin_fill()
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()
###################################################################
def draw_oval(radius, color, thickness=1, position=(0, 0)):
    t = Turtle()
    # up the pen and move to the position and down the pen again to draw
    t.penup()
    t.goto(position)
    t.pendown()
    # set the color and thickness
    t.color(color)
    t.pensize(thickness)
    # draw the oval using and fill it
    t.begin_fill()
    t.left(45)
    for i in range(2):
        t.circle(radius, 90)
        t.circle(radius / 2, 90)
    t.end_fill()
###################################################################
def draw_triangle():
    size = int(input("Enter the size of the triangle: "))
    color = input("Enter the color of the triangle: ")
    thickness = int(input("Enter the thickness of the triangle: "))
    x = int(input("Enter the x position of the triangle: "))
    y = int(input("Enter the y position of the triangle: "))
    draw_shape(3, size, color, thickness, (x, y))
###################################################################
def draw_square():
    size = int(input("Enter the size of the square: "))
    color = input("Enter the color of the square: ")
    thickness = int(input("Enter the thickness of the square: "))
    x = int(input("Enter the x position of the square: "))
    y = int(input("Enter the y position of the square: "))
    draw_shape(4, size, color, thickness, (x, y))
###################################################################
def draw_pentagon():
    size = int(input("Enter the size of the pentagon: "))
    color = input("Enter the color of the pentagon: ")
    thickness = int(input("Enter the thickness of the pentagon: "))
    x = int(input("Enter the x position of the pentagon: "))
    y = int(input("Enter the y position of the pentagon: "))
    draw_shape(5, size, color, thickness, (x, y))
###################################################################
def draw_hexagon():
    size = int(input("Enter the size of the hexagon: "))
    color = input("Enter the color of the hexagon: ")
    thickness = int(input("Enter the thickness of the hexagon: "))
    x = int(input("Enter the x position of the hexagon: "))
    y = int(input("Enter the y position of the hexagon: "))
    draw_shape(6, size, color, thickness, (x, y))
###################################################################
def main():
    ##########################################
    print("################")
    print("draw a star")
    print("################")
    draw_star(3, "brown", 150, 2, (-50, 0))
    ##########################################
    print("################")
    print("draw a circle")
    print("################")
    draw_circle(100, "purple", 2, (250, 100))
    ##########################################
    print("################")
    print("draw an oval")
    print("################")
    draw_oval(100, "red", 2, (250, -200))
    ##########################################
    print("################")
    print("draw an rectangle")
    print("################")
    draw_rectangle(150, 100, "navy", 2, (-200, -150))
    ##########################################
    print("################")
    print("draw a triangle")
    print("################")
    draw_shape(3, 100, "green", 2, (0, -200))
    ##########################################
    print("################")
    print("draw a square")
    print("################")
    draw_shape(4, 100, "red", 3, (-50, 125))
    ##########################################
    print("################")
    print("draw a pentagon")
    print("################")
    draw_shape(5, 100, "blue", 4, (300, -50))
    ###########################################
    print("################")
    print("draw a hexagon")
    print("################")
    draw_shape(6, 100, "brown", 5, (-250, 0))
    #########################################
    exitonclick()
    #########################################

if __name__ == "__main__":
    main()
