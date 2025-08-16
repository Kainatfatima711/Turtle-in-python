import turtle

turtle.Screen().bgcolor("Purple")
pen = turtle.Turtle()

# first triangle for star
pen . forward(100) # draw base

pen . left(120)
pen . forward(100)

pen . left(120)
pen . forward(100)

pen . penup()
pen . right(150)
pen . forward(50)

#Second triangle for star
pen . pendown()
pen . right(90)
pen . forward(100)

pen . right(120)
pen . forward(100)

pen . right(120)
pen . forward(100)

turtle . done()


