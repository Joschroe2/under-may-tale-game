from gturtle import *

def textSqaure():
    te1.hideTurtle()
    te1.setPos(200,275)
    te1.setPenColor("white")
    te1.setFillColor("white")
    te1.startPath()
    repeat 2:
        te1.fd(200)
        te1.rt(90)
        te1.fd(250)
        te1.rt(90)
    te1.fillPath()
    
def text1():
    dia.textSquare()
    te1.setPos(250,330)
    te1.setFontSize(18)
    te1.setPenColor("black")
    te1.label("hello world")