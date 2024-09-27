from gturtle import *

def at1(pTurtle):
    pTurtle.setPos(0,-230)
    pTurtle.setPenColor("red")
    pTurtle.setPenWidth(10)
    repeat 16:
        pTurtle.fd(80)
        pTurtle.rt(36)
        delay(200)
    pTurtle.setPos(0,-230)
    pTurtle.setPenColor("white")
    repeat 16:
        pTurtle.fd(80)
        pTurtle.rt(36)
        delay(200)
        c1.getPixelColorStr()
        if pixelColorStr == "white":
            health.fd(7)
    pTurtle.setPos(0,-230)
    pTurtle.setPenColor("black")
    delay(300)
    repeat 16:
        pTurtle.fd(80)
        pTurtle.rt(36)
        
def at2(pTurtle):
    pTurtle.setHeading(0)
    pTurtle.setPenColor("red")
    pTurtle.setPenWidth(
    pTurtle.bk(140)
    pTurtle.fd(240)