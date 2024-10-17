from gturtle import *
     
def fight(pTurtle):
    repaint()
    pTurtle.setFillColor("black")
    pTurtle.fill()
    pTurtle.setPos(-140,-140)
    pTurtle.setHeading(0)
    pTurtle.setPenWidth(8)
    pTurtle.setFillColor("black")
    pTurtle.setPenColor("white")
    
    repeat 4:
        pTurtle.fd(280)
        pTurtle.rt(90)
        
    
    
    c = 1
    repeat 4:
        pTurtle.setPenColor("orange")
        pTurtle.setPenWidth(8)
        repeat 4:
            if c == 1:
                pTurtle.setPos(-270,-400)
                repeat 2:
                    pTurtle.forward(90)
                    pTurtle.right(90)
                    pTurtle.forward(220)
                    pTurtle.right(90)
                c = c + 1
                pTurtle.setFontSize(50)
                pTurtle.setPos(-190,-370)
                pTurtle.label("Act")
            elif c == 2:
                pTurtle.setPos(-550,-400)
                repeat 2:
                    pTurtle.forward(90)
                    pTurtle.right(90)
                    pTurtle.forward(220)
                    pTurtle.right(90)
                pTurtle.setPos(-470,-370)
                pTurtle.label("Fight")
                c = c + 1
            elif c == 3:
                pTurtle.setPos(20,-400)
                repeat 2:
                    pTurtle.forward(90)
                    pTurtle.right(90)
                    pTurtle.forward(220)
                    pTurtle.right(90)
                pTurtle.setPos(100,-370)
                pTurtle.label("Pizza")
                c = c + 1
            elif c == 4:
                pTurtle.setPos(300,-400)
                repeat 2:
                    pTurtle.forward(90)
                    pTurtle.right(90)
                    pTurtle.forward(220)
                    pTurtle.right(90)
                pTurtle.setPos(370,-370)
                pTurtle.label("Spare")
                c = c + 1
    
def pause(pTurtle):
    repaint()
    pTurtle.setFillColor("black")
    pTurtle.fill()
    pTurtle.setPos(-500,-200)
    pTurtle.setPenWidth(12)
    pTurtle.setFillColor("black")
    pTurtle.setPenColor("white")
    pTurtle.startPath()
    pTurtle.rt(90)
    repeat 2:
        pTurtle.fd(1000)
        pTurtle.lt(90)
        pTurtle.fd(240)
        pTurtle.lt(90)
    pTurtle.fillPath()
    pTurtle.lt(90)
    c = 1
    repeat 4:
        pTurtle.setPenColor("orange")
        pTurtle.setPenWidth(8)
        repeat 4:
            if c == 1:
                pTurtle.setPos(-270,-400)
                repeat 2:
                    pTurtle.forward(90)
                    pTurtle.right(90)
                    pTurtle.forward(220)
                    pTurtle.right(90)
                c = c + 1
                pTurtle.setFontSize(50)
                pTurtle.setPos(-190,-370)
                pTurtle.label("Act")
            elif c == 2:
                pTurtle.setPos(-550,-400)
                repeat 2:
                    pTurtle.forward(90)
                    pTurtle.right(90)
                    pTurtle.forward(220)
                    pTurtle.right(90)
                pTurtle.setPos(-470,-370)
                pTurtle.label("Fight")
                c = c + 1
            elif c == 3:
                pTurtle.setPos(20,-400)
                repeat 2:
                    pTurtle.forward(90)
                    pTurtle.right(90)
                    pTurtle.forward(220)
                    pTurtle.right(90)
                pTurtle.setPos(100,-370)
                pTurtle.label("Item")
                c = c + 1
            elif c == 4:
                pTurtle.setPos(300,-400)
                repeat 2:
                    pTurtle.forward(90)
                    pTurtle.right(90)
                    pTurtle.forward(220)
                    pTurtle.right(90)
                pTurtle.setPos(370,-370)
                pTurtle.label("Mercy")
                c = c + 1

def gb(pTurtle):
    pTurtle.setPos(270,0)
    pTurtle.setHeading(0)
    pTurtle.setPenWidth(8)
    pTurtle.setPenColor("white")
    pTurtle.setFillColor("black")
    pTurtle.startPath()
    repeat 2:
        pTurtle.fd(400)
        pTurtle.rt(90)
        pTurtle.fd(320)
        pTurtle.rt(90)
    pTurtle.fillPath()

 
def gbr(pTurtle):
    pTurtle.setPos(270,0)
    pTurtle.setHeading(0)
    pTurtle.setPenWidth(8)
    pTurtle.setPenColor("black")
    pTurtle.setFillColor("black")
    pTurtle.startPath()
    repeat 2:
        pTurtle.fd(400)
        pTurtle.rt(90)
        pTurtle.fd(320)
        pTurtle.rt(90)
    pTurtle.fillPath()

def plpr(pTurtle):
    pTurtle.setPenColor("black")
    pTurtle.setPos(-75,-225)
    pTurtle.setFillColor("black")
    pTurtle.startPath()
    pTurtle.setHeading(90)
    repeat 2:
        pTurtle.fd(200)
        pTurtle.lt(90)
        pTurtle.fd(50)
        pTurtle.lt(90)
    pTurtle.fillPath()
    pTurtle.setHeading(0)
    
def ded(pTurtle):
    global res
    res = 1
    clear("black")
    pTurtle.setPos(-50,0)
    pTurtle.setFontSize(69)
    pTurtle.setPenColor("white")
    while res == 1:
        pTurtle.label("YOU DIED!")
        delay(5000)
        res = 0
        
def bKill(pTurtle):
    clear("black")
    pTurtle.setPos(-300,0)
    pTurtle.setPenColor("white")
    pTurtle.setFontSize(69)
    pTurtle.label("You defeated your own brother")
    delay(6000)
    clear("black")

def yKill(pTurtle):
    clear("black")
    pTurtle.setPos(-280,0)
    pTurtle.setPenColor("white")
    pTurtle.setFontSize(69)
    pTurtle.label("Your brother defeated you")
    pTurtle.setPos(-420,-80)
    pTurtle.label("and became the new demon king")
    delay(6000)
    clear("black")