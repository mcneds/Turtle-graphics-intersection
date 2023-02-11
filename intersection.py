#init perameters
import turtle
import sys
import math
sys.setExecutionLimit(10000000)
#init window
wn = turtle.Screen()

#initialize turtles
roadH = turtle.Turtle()
roadV = turtle.Turtle()
roadMarkings = turtle.Turtle()
car1 = turtle.Turtle()
car2 = turtle.Turtle()
car3 = turtle.Turtle()
car4 = turtle.Turtle()
wheel = turtle.Turtle()
stopSign = turtle.Turtle()
tree = turtle.Turtle()
#set turtle speeds

roadH.speed(10)
roadV.speed(10)
roadMarkings.speed(10)
car1.speed(10)
car2.speed(10)
car3.speed(10)
car4.speed(10)
wheel.speed(10)
stopSign.speed(10)
tree.speed(10)

#set turtle colors
roadH.pencolor("#494a4a")#dark grey
roadV.pencolor("#494a4a")#dark grey
roadH.fillcolor("#494a4a")#dark grey
roadV.fillcolor("#494a4a")#dark grey
roadMarkings.pencolor("#15f505")#yellow
roadMarkings.fillcolor("#15f505")#yellow
car1.pencolor("#f00a0a")#red
car2.pencolor("#0a24f0")#blue
car3.pencolor("#0a24f0")#blue
car4.pencolor("#0a24f0")#blue
car1.fillcolor("#f00a0a")#red
car2.fillcolor("#0a24f0")#blue
car3.fillcolor("#0a24f0")#blue
car4.fillcolor("#0a24f0")#blue
wheel.pencolor("#0a0a0a")#black
wheel.fillcolor("#0a0a0a")#black
stopSign.pencolor("#f50000")#red
stopSign.fillcolor("#f50000")#red
wn.bgcolor("#039e08")#green

#start roads
#horizontal road
roadH.penup()
roadH.left(90)
roadH.forward(50)
roadH.pendown()

roadH.begin_fill()
roadH.right(90)
roadH.forward(200)
roadH.right(90)
roadH.forward(100)
roadH.right(90)
roadH.forward(400)
roadH.right(90)
roadH.forward(100)
roadH.right(90)
roadH.forward(200)
roadH.end_fill()

#vertical road

roadV.begin_fill()
roadV.backward(50)
roadV.left(90)
roadV.forward(200)
roadV.right(90)
roadV.forward(100)
roadV.right(90)
roadV.forward(400)
roadV.right(90)
roadV.forward(100)
roadV.right(90)
roadV.forward(200)
roadV.end_fill()

#road markings center yellow
roadMarkings.width(5)
for i in range(4):
    roadMarkings.up()
    roadMarkings.forward(50)
    roadMarkings.pendown()
    roadMarkings.forward(30)
    roadMarkings.penup()
    roadMarkings.forward(30)
    roadMarkings.pendown()
    roadMarkings.forward(30)
    roadMarkings.penup()
    roadMarkings.forward(30)
    roadMarkings.pendown()
    roadMarkings.forward(30)
    roadMarkings.penup()
    roadMarkings.goto(0,0)
    roadMarkings.left(90)
roadMarkings.up()
roadMarkings.home()
roadMarkings.pencolor("#f0f0f0")#white
roadMarkings.fillcolor("#f0f0f0")#white
roadMarkings.pensize(3)
#cross walks
for i in range(4):
    roadMarkings.up()
    roadMarkings.right(45)
    roadMarkings.forward(70)
    roadMarkings.right(45)
    roadMarkings.down()
    for i in range (9):
        roadMarkings.right(90)
        roadMarkings.up()
        roadMarkings.forward(10)
        roadMarkings.down()
        roadMarkings.left(90)
        roadMarkings.forward(20)
        roadMarkings.up()
        roadMarkings.backward(20)
        roadMarkings.down()
    roadMarkings.up()
    roadMarkings.goto(0,0)
    roadMarkings.down()







    
def drawCar(t, carX, carY, carRot):
   
    #move car  pens
    
    t.up()
    t.goto(carX,carY)
    t.right(carRot)
    t.down()
    carPos = t.pos()
    
    #move wheel pens
    wheel.up()
    wheel.home()
    wheel.goto(carPos)
    wheel.right(carRot)
    wheel.down()
    #draw wheels for car 

    wheel.begin_fill()
    wheel.circle(5)
    wheel.end_fill()
    wheel.up()
    wheel.forward(33)
    wheel.down()
    wheel.begin_fill()
    wheel.circle(5)
    wheel.end_fill()
    wheel.up()
    wheel.home()
    #draw car body

    windshieldLength = int(8.48528137424)
    t.begin_fill()
    t.forward(40)
    t.right(90)
    t.forward(7)
    t.right(90)
    t.forward(6)
    t.left(45)
    t.forward(windshieldLength)
    t.right(45)
    t.forward(10)
    t.right(45)
    t.forward(windshieldLength)
    t.left(45)
    t.forward(13)
    t.right(90)
    t.forward(7)
    t.end_fill()
    
    
    
    
#car function calls
drawCar(car1, -25, 120, 270)
drawCar(car2, 25, -120, 90)
drawCar(car3, 120, -25, 180)
drawCar(car4, -120, -25, 180)
#stop sign

for i in range(4):
    stopSign.penup()
    stopSign.left(45)
    stopSign.forward(85)
    stopSign.left(45)
    stopSign.pendown()
    stopSign.forward(50)
    #move into place for circle
    stopSign.forward(5)
    stopSign.right(90)
    stopSign.begin_fill()
    stopSign.circle(16)
    stopSign.end_fill()
    stopSign.left(90)
    stopSign.forward(8)
    stopSign.pencolor("#ffffff")#white
    stopSign.write("stop", font=('Arial', 4, 'bold'))
    stopSign.pencolor("#f50000")#red
    stopSign.penup()
    stopSign.goto(0,0)
    
#function to draw trees
def drawTree(t, treeX, treeY, trunkWidth, trunkHeight, leafSectionWidth, leafNumSections, trunkColor, leafColor, sectionSeperation, taper):
    t.pencolor(trunkColor)
    t.fillcolor(trunkColor)
    t.up()
    t.goto(treeX, treeY)
    t.down()
    t.begin_fill()
    for i in range(2):
        t.forward(trunkWidth)
        t.left(90)
        t.forward(trunkHeight)
        t.left(90)
    t.end_fill()
    t.up()
    t.left(90)
    t.forward(trunkHeight)
    t.right(90)
    t.forward(trunkWidth / 2)
    t.pendown()              
    t.fillcolor(leafColor)
    t.pencolor(leafColor)              
    
    for i in range(leafNumSections):
        t.begin_fill()
        t.forward(math.sqrt(2) * leafSectionWidth / 2)
        t.left(135)
        t.forward(leafSectionWidth)
        t.left(90)
        t.forward(leafSectionWidth)
        t.left(135)
        t.forward(math.sqrt(2) * leafSectionWidth / 2)
        t.end_fill()
        t.up()
        t.left(90)
        triHeight = int(leafSectionWidth - (leafSectionWidth * ((math.sqrt(2))/2)) + sectionSeperation)
        t.forward(triHeight)
        t.right(90)
        t.down()
        leafSectionWidth -= taper

    
#tree test
drawTree(tree, 130, 100, 7, 15, 40, 3, "#1f1201", "#02520e", 5, 10) 
drawTree(tree, -130, -140, 7, 15, 40, 6, "#1f1201", "#02520e", 3, 5)

    
#hide turtles
roadH.hideturtle()
roadV.hideturtle()
car1.hideturtle()
car2.hideturtle()
car3.hideturtle()
car4.hideturtle()
wheel.hideturtle()
stopSign.hideturtle()
tree.hideturtle()
roadMarkings.hideturtle()
wn.exitonclick()