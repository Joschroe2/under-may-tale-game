from gturtle import *

"erstellt hello world text"   
def text1():
    te1.setPos(250,300)
    te1.setFontSize(18)
    te1.setPenColor("white")
    te1.label("hello world")
    delay(80)
    te1.setFillColor("black")
    te1.fillPath()

"stellt die fenstergröße und position ein"
setFramePositionCenter()
Options.setPlaygroundSize(1200,900)

"setzt die Turtle c1 zum Maus-Zeiger"
def onMouseMoved(x,y):
    if x > -100:
        if x < 100:
            if y > -235:
                if y < -45:
                    c1.setPos(x,y)
    
"erstellt die verschiedenen Turtles"
c1 = makeTurtle(mouseMoved = onMouseMoved)
c1.setColor("red")
t1 = Turtle(c1,"white")
te1 = Turtle(c1,"white")
box = Turtle(c1,"white")
at = Turtle(c1,"blue")
at.hideTurtle()

c1.setPos(0,-140)

"setzt Farbe und Position von t1 fest"
t1.setFillColor("black")
t1.setPos(0,200)
t1.fill()

"setzt Position von te1 fest und gibt den befehl text1"
te1.setPos(250,300)
te1.hideTurtle()
text1()

"erstellt einen Kasten in dem sich der spieler befinden kann"
box.setPos(-110,-250)
box.hideTurtle()
box.setPenColor("white")
box.setPenWidth(8)
box.setFillColor("black")
box.startPath()
repeat 4:
    box.forward(220)
    box.rt(90)
box.fillPath()

"Leben:"
health = Turtle(c1)
health.hideTurtle()
health.setPos(-300,-300)
health.lt(90)
health.setPenColor("red")
health.setPenWidth(20)

"erstellt eine Attacke1"
def at1():
    at.setPenColor("red")
    at.setPos(-80,-120)
    at.setPenWidth(10)
    at.rt(45)
    repeat 15:
        at.fd(200)
        at.rt(13)
        at.lt(260)
        delay(100)
    delay(200)
    at.setHeading(0)
    at.setPenColor("white")
    at.setPos(-80,-120)
    at.setPenWidth(10)
    at.rt(45)
    for i in range(38):
        at.fd(200)
        at.rt(13)
        at.lt(260)
        delay(130)
        c1.getPixelColorStr()
        if c1.pixelColorStr == "white":
            health.fd(13)
        if i == 16:
            at.setPos(-80,-120)
            at.setHeading(0)
            at.rt(45)
            at.setPenColor("black")
delay(800)
at1()