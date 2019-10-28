# print("This will execute first")

# for _ in range(3):
#     print("Tthis line will execute three times")
#     print("This line will also execute three times")

# print("Now we are outside of the for loop!")    

import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")

dist = 5
tess.up()
for _ in range(30):
    tess.stamp()
    tess.forward(dist)
    tess.right(24)
    dist = dist + 2
window.exitonclick()



# import random

# prob = random.random()
# print(prob)

# diceThrow = random.randrange(1,7)
# print(diceThrow)
