from gturtle import *
import webbrowser
 
mm = makeTurtle()
mm.hideTurtle()
mm.setFillColor("black")
mm.fill()

def go(pTurtle):
    repaint()
    pTurtle.setPos(-200,0)
    pTurtle.setFontSize(69)
    pTurtle.setPenColor("white")
    pTurtle.label("GAME OVER")
    delay(1500)
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    
go(mm)