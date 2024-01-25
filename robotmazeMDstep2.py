#   a115_robot_maze.py
import turtle as trtl

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
def move():
  robot.dot(10)
  robot.fd(50)

def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)

def turn_right():
  robot.speed(0)
  robot.rt(90)
  robot.speed(2)
  
  
  
def resetposition():
    robot.setx(startx)
    robot.sety(starty)
    robot.color("darkorchid")
    robot.pencolor("darkorchid")
    robot.clear()

def maze1method():
  for i in range(4):
    move()
  turn_right()
  for i in range(4):
    move()

def maze2method1():
  for i in range(3):
    move()
  turn_right()
  for i in range(2):
    move()

def maze2method2():
  robot.color("orange")
  robot.pencolor("orange")
  for i in range(2):
    for i in range(3):
      move()
    turn_left()
  move()
  
def maze3method():
    turn_right()
    move()
    turn_left()
    for i in range (2):
        move()
    turn_right()
    move()
    robot.color("orange")
    robot.pencolor("orange")
    move()
    turn_left()
    for i in range (2):
        move()
    turn_right()
    move()

#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "robot.gif"
wn.addshape(robot_image)

#----- init robot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

#---- TODO: change maze here
wn.bgpic("maze1.png") # other file names should be maze2.png, maze3.png

#---- TODO: begin robot movement here
# move robot forward with move()
while True:
    wn.bgpic("maze1.png")
    maze1method()
    resetposition()
    wn.bgpic("maze2.png")
    turn_left()
    maze2method1()
    resetposition()
    maze2method2()
    resetposition()
    wn.bgpic("maze3.png")
    for i in range(3):
      turn_left()
    maze3method()
    resetposition()
    turn_left()
# sample for loop:
'''
for step in range(3): # forward 3
  move()
'''

#---- end robot movement 

wn.mainloop()