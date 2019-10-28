import turtle
wn = turtle.Screen()

elan = turtle.Turtle()

distance = 50
for i in range(10):
    elan.forward(distance)
    elan.right(90)
    distance = distance + 10
    