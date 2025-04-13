from turtle import Turtle, Screen

Sam = Turtle("turtle")
Sam.color("red")
Window = Screen()
Sam.speed("fastest")
for _ in range(4):
    Sam.forward(100)
    Sam.left(90)
    

Window.exitonclick() 