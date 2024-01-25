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
  
def moveRight():
  robot.rt(90)
  move()
  robot.lt(90)

def moveLeft():
  robot.lt(90)
  move()
  robot.rt(90)

def moveDown():
  robot.rt(180)
  move()
  robot.rt(180)
  
  
def resetposition():
    robot.setx(startx)
    robot.sety(starty)
    robot.color("darkorchid")
    robot.pencolor("darkorchid")
    robot.clear()
    
# KEY STROKES AND INPUTS
trtl.onkeypress(move,"w")     #Keyboard bindings from the window object       
trtl.onkeypress(moveDown,"s")   #Keyboard bindings from the window object       
trtl.onkeypress(moveLeft,"a")   #Keyboard bindings from the window object       
trtl.onkeypress(moveRight,"d")  #Keyboard bindings from the window object
trtl.listen()                 #Tells the window to listen for key presses

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
wn.bgpic("maze4.png") # other file names should be maze2.png, maze3.png

#---- TODO: begin robot movement here

# sample for loop:
'''
for step in range(3): # forward 3
  move()
'''

#---- end robot movement 

wn.mainloop()
