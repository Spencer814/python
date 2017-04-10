import turtle
import random

def draw_shapes(size):
  window = turtle.Screen()
  window.bgcolor("black")
  
  soph = turtle.Turtle()
  izzy = turtle.Turtle()
  alex = turtle.Turtle()
  angle = 120

  turtles = [soph, izzy, alex]
  
  for name in turtles:
    name.shape("turtle")
    name.speed(6)
    name.color(random.random(), random.random(), random.random())
  
  for side in range(6):
    soph.fd(size * 0.95)
    soph.lt(angle / 2)
    soph.fd(size * 0.95)
    soph.rt(angle)
  
  for side in range(5):
    izzy.rt(angle)
    izzy.fd(size)
    izzy.rt(72 - angle)
    izzy.fd(size)

  alex.lt(angle / 0.5)
  for side in range(8):
    alex.rt(angle)
    alex.fd(size * 0.75)
    alex.lt(angle - 45)
    alex.fd(size * 0.75)
  
  window.exitonclick()
  
draw_shapes(100)