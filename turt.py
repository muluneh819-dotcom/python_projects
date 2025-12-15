import turtle
import time

def myfun():
    colors = ["red", "blue", "green", "yellow", "orange", "brown"]
    
    t = turtle.Turtle()        
    screen = turtle.Screen()   
    
    t.pensize(5)
    screen.bgcolor("black")
    t.speed(0)                 
    
    for x in range(360):
        t.pencolor(colors[x % len(colors)])
        t.pensize(x / 50)
        t.forward(x)
        t.left(59)

myfun()
time.sleep(5)

