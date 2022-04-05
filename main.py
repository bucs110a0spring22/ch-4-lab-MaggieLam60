import math
import turtle

########### Code here ##############


def drawSineCurve(grapher):
    '''
  general function description: this makes the sin graph, then goes to the next graph
  args: graphers, turtle that makes the graph
  return: none
  '''
    for xCord in range(-360, 361):
        yCord = math.sin(math.radians(xCord))
        grapher.goto(xCord, yCord)
    grapher.up()
    yCord = math.cos(math.radians(-360))
    grapher.goto(-360, yCord)


#Part B
def setupWindow(mywindow=None):
    '''
  general function description: sets the window and the general coordinates
  args: myCordwindow, window name
  return: none
  '''
    mywindow.bgcolor("orange")
    mywindow.setworldcoordinates(-360, -1, 360, 1)


def setupAxis(myturtle=None):
    '''
general function description: creates the axis for the graphs
args: myturtle, also grapher, makes the axis 
return: none
'''
    myturtle.reset()
    myturtle.speed(0)
    myturtle.goto(0, 0)
    myturtle.goto(0, -500)  #this is for other functions
    myturtle.goto(0, 500)
    myturtle.goto(0, 0)
    myturtle.goto(360, 0)
    myturtle.goto(-360, 0)


def drawCosineCurve(grapher):
    '''
general function description: draws the cos graph then goes onto the next graph location 
args: graphers, turtle that makes the graph
return: none
'''
    grapher.down()
    for xCord in range(-360, 361):
        yCord = math.cos(math.radians(xCord))
        grapher.goto(xCord, yCord)
    grapher.up()
    yCord = math.tan(math.radians(-360))
    grapher.goto(-360, yCord)


def drawTangentCurve(grapher):
    '''
general function description: draws the tangent graph 
args: graphers, turtle that makes the graph
return: none
'''
    grapher.down()
    for xCord in range(-360, 361):
        yCord = math.tan(math.radians(xCord))
        grapher.goto(xCord, yCord)
    grapher.up()
    grapher.clear()


#Three Functions
#1 addition function
def drawParabola(grapher, mywindow):
    '''
general function description: makes a parabola graph
args: graphers, makes the parabola shape, mywindow, makes color
return: none
'''
    setupAxis(grapher)
    mywindow.bgcolor("light blue")
    mywindow.setworldcoordinates(-20, 0, 20, 400)
    grapher.down()
    for xCord in range(-20, 21):
        yCord = xCord**2
        grapher.goto(xCord, yCord)
    grapher.up()


#addition feature with parameters
def drawAbsValue(grapher, mywindow):
    '''
general function description: draws an abs value graph
args: graphers, turtle that makes the graph, mywindow, makes window color
return: none
'''
    setupAxis(grapher)
    mywindow.bgcolor("light green")
    mywindow.setworldcoordinates(-200, 0, 200, 300)
    grapher.down()
    for xCord in range(-250, 251):
        yCord = abs(xCord)
        grapher.goto(xCord, yCord)
    grapher.up()


#addition feature with return
def fibonacci(nterm):
    '''
general function description: function to set up fibonacci sequence
args: graphers, turtle that makes the graph, nterm the placement within the fib sequence 
return: 1, fibonacci(nterm-1), fibonacci(nterm-2), returns the values of the previous turn, the turn before that, and the first 2 turns
'''
    if nterm == 1 or nterm == 2:
        return 1
    else:
        return fibonacci(nterm - 1) + fibonacci(nterm - 2)


def drawFib(grapher, window, nterm):
    '''
general function description: draws the fibonacci graph
args: graphers: a turtle that makes the graph, nterm: the placement within sequence, window: the background 
return: fibHelper(grapher,window,n), axCordis set up
'''
    grapher.clear()
    window.setworldcoordinates(0, 0, 10, 10)
    grapher.speed(1)
    grapher.up()
    grapher.goto(0, 0)
    grapher.down()
    grapher.goto(nterm, 0)
    grapher.up()
    grapher.goto(0, 0)
    grapher.down()
    return fibHelper(grapher, window, nterm)


def fibHelper(grapher, window, nterm):
    '''
general function description: 
args: graphers: a turtle that makes the graph, nterm: the placement within sequence, window: the background 
return yCord, gives the fibonacci number at that place within the sequence, and the graph 
'''
    max = 0
    for term in range(1, nterm + 1):
        yCord = fibonacci(term)
        grapher.goto(term, yCord)
        if yCord > max:
            max = yCord
            window.setworldcoordinates(0, 0, nterm + 2, max + 2)
            grapher.up()
            grapher.goto(0, 0)
            grapher.down()
            grapher.goto(0, yCord)
            grapher.up()
            grapher.goto(term, yCord)
            grapher.down()
        if term == nterm:
            return yCord


##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(2)
    grapher = turtle.Turtle()
    shape = int(
        input(
            "Give us a number from 0-3 and we'll draw with a different shape: ")
    )
    if shape < 0 or shape > 3:
        shape = int(
            input(
                "Give us a number from 0-3 and we'll draw with a different shape: "
            ))

    if shape == 0:
        grapher.shape("classic")
    elif shape == 1:
        grapher.shape("turtle")
    elif shape == 2:
        grapher.shape("circle")
    elif shape == 3:
        grapher.shape("square")

    drawSineCurve(grapher)

    #Part B
    setupWindow(wn)
    setupAxis(grapher)
    grapher.speed(0)
    drawSineCurve(grapher)
    drawCosineCurve(grapher)
    drawTangentCurve(grapher)
    input("Press Enter for next curve ")
    drawParabola(grapher, wn)
    input("Press Enter for next curve ")
    drawAbsValue(grapher, wn)
    nterm = int(input("Input integer > 0: "))
    if nterm < 1:
        nterm = int(input("Input integer > 0: "))

    nthTerm = drawFib(grapher, wn, nterm)

    print("The " + str(nterm) + "th term of the fibonacci sequence is: " +
          str(nthTerm))
    wn.exitonclick()


main()
