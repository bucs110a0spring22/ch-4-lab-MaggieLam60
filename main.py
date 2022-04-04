import math
import turtle

########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help


# fred.goto(100,100)
# fred.goto(100,-100)
# fred.goto(-100,100)
# fred.goto(-100,-100)

def drawSineCurve(dart):
  for x in range(-360,361):
    y= math.sin(math.radians(x))
    dart.goto(x,y)
  dart.up()
  y = math.cos(math.radians(-360))
  dart.goto(-360,y)


#Part B

def setupWindow(mywindow=None):
  mywindow.bgcolor("orange")
  mywindow.setworldcoordinates(-360,-1,360,1)

def setupAxis(myturtle=None):
  myturtle.reset()
  myturtle.speed(0)
  myturtle.goto(0,0) 
  myturtle.goto(0,-1)
  myturtle.goto(0,1)
  myturtle.goto(0,0)
  myturtle.goto(360,0)
  myturtle.goto(-360,0)

def drawCosineCurve(dart):
  dart.down()
  for x in range(-360,361):
    y= math.cos(math.radians(x))
    dart.goto(x,y)
  dart.up()
  y = math.tan(math.radians(-360))
  dart.goto(-360,y)

def drawTangentCurve(dart):
  dart.down()
  for x in range(-360,361):
    y= math.tan(math.radians(x))
    dart.goto(x,y)







##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()
