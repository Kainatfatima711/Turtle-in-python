import turtle # Library

turtle.Screen().bgcolor("orange")
turtle.Screen().setup( 300 , 400 )

pen = turtle.Turtle()

num_sides = 4
side_length = 70
angle = 90

for i in range( 4 ): #0,1,2,3
    pen.forward(side_length)
    pen.right(angle)

turtle.done