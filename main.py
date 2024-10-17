from gturtle import *
import backgrounds
import attacks
import texts


"stellt die Größe des Fensters ein"
setFramePositionCenter()
Options.setPlaygroundSize(1300,900)


"erstellt die Maussteuerung"
def onMouseMoved(x,y):
    global lp
    global plp
    global damage
    if x > -131:
        if x < 131:
            if y > -128:
                if y < 128:
                    t1.setPos(x,y)  
    farbe = getPixelColorStr()
    if farbe == "white":
        lp = lp + damage

damage = 3        

def onKeyPressed(key):
    global mp
    global tp
    global acpt
    if mp == 1:
        if key == 37:
            if tp == 1:
                tp = 4
            else:
                tp = tp - 1
        if key == 39:
            if tp == 4:
                tp = 1
            else:
                tp = tp + 1
        if key == 32:
            acpt = 1
            delay(10)
            acpt = 0
    
def end(pTurtle):
    global lp
    pTurtle.setFontSize(69)
    pTurtle.setPos(0,0)
    pTurtle.setPenColor("yellow")
    pTurtle.label(lp)
    pTurtle.setPos(120,50)
    pTurtle.startPath()
    pTurtle.setFillColor("black")
    delay(1000)
    if lp > 250:
        clear("black")
        pTurtle.setPenColor("yellow")
        setPos(120,50)
        setFontSize(69)
        label("D")
        setPos(50,-50)
        setFontSize(26)
        label("Dismal!")
    elif lp < 250:
        clear("black")
        pTurtle.setPenColor("yellow")
        pTurtle.setPos(120,50)
        pTurtle.setFontSize(69)
        pTurtle.label("C")
        pTurtle.setPos(50,-50)
        pTurtle.setFontSize(26)
        pTurtle.label("Crazy!")
        if lp < 200:
            clear("black")
            pTurtle.setPenColor("yellow")
            pTurtle.setPos(120,50)
            pTurtle.setFontSize(69)
            pTurtle.label("B")
            pTurtle.setPos(50,-50)
            pTurtle.setFontSize(26)
            pTurtle.label("Badass!")
            if lp < 150:
                clear("black")
                pTurtle.setPenColor("yellow")
                pTurtle.setPos(120,50)
                pTurtle.setFontSize(69)
                pTurtle.label("A")
                pTurtle.setPos(50,-50)
                pTurtle.setFontSize(26)
                pTurtle.label("Apocalyptic!")
                if lp < 100:
                    clear("black")
                    pTurtle.setPenColor("yellow")
                    pTurtle.setPos(120,50)
                    pTurtle.setFontSize(69)
                    pTurtle.label("S")
                    pTurtle.setPos(50,-50)
                    pTurtle.setFontSize(26)
                    pTurtle.label("Savage!")
                    if lp < 50:
                        clear("black")
                        pTurtle.setPenColor("yellow")
                        pTurtle.setPos(120,50)
                        pTurtle.setFontSize(69)
                        pTurtle.label("SS")
                        pTurtle.setPos(50,-50)
                        pTurtle.setFontSize(26)
                        pTurtle.label("Sick Skills!")
                        if lp <= 0:
                            clear("black")
                            pTurtle.setPenColor("yellow")
                            pTurtle.setPos(120,50)
                            pTurtle.setFontSize(69)
                            pTurtle.label("SSS")
                            pTurtle.setPos(50,-50)
                            pTurtle.setFontSize(26)
                            pTurtle.label("Smokin' Sexy Style!")

def a9(pTurtle):
    global dlp
    pTurtle.setPenColor("white")
    pTurtle.setPenWidth(280)
    pTurtle.setPos(280,0)
    pTurtle.setHeading(270)
    if dlp < 200:
        repeat 235:
            pTurtle.fd(1)
            delay(30)
        delay(6000)
    else:
        repeat 300:
            pTurtle.fd(1)
            delay(30)
        delay(6000)

def a9e(pTurtle):
    global dlp
    pTurtle.setPenColor("white")
    pTurtle.setPenWidth(280)
    pTurtle.setPos(280,0)
    pTurtle.setHeading(270)
    repeat 300:
        pTurtle.fd(1)
        delay(30)
    delay(6000)


mp = 0 
tp = 1
acpt = 0
dlp = 1000

res = 0
     
def mpp(pTurtle):
    global mp
    global tp
    global acpt
    global lp
    global dlp
    global damage
    mp = 1
    while mp == 1:
        if tp == 1:
            t1.setPos(-505,-355)
            if acpt == 1:
                dlp = dlp - 203
                if dlp < 0:
                    dlp = 0
                mp = 0
                t1.setPos(0,0)
                backgrounds.gb(t5)
                ate(t5)
                delay(3000)
                backgrounds.gbr(t5)
                delay(1000)
        elif tp == 2:
            t1.setPos(-225,-355)
            if acpt == 1:
                mp = 0
                damage = damage + 3
                t1.setPos(0,0)
                backgrounds.gb(t5)
                texts.actte(t5)
                delay(3000)
                backgrounds.gbr(t5)
                delay(1000)
        elif tp == 3:
            t1.setPos(65,-355)
            if acpt == 1:
                lp = lp - 23
                mp = 0
                t1.setPos(0,0)
                backgrounds.gb(t5)
                texts.pizza(t5)
                delay(6000)
                backgrounds.gbr(t5)
                delay(1000)
        elif tp == 4:
            t1.setPos(345,-355)
            if acpt == 1:
                mp = 0
                t1.setPos(0,0)            
                backgrounds.gb(t5)
                texts.sTe(t5)
                delay(4000)
                backgrounds.gbr(t5)
                delay(1000)

def mppE(pTurtle):
    global mp
    global tp
    global acpt
    global lp
    global dlp
    global damage
    mp = 1
    backgrounds.gb(t5)
    texts.finDec(t5)
    while mp == 1:
        if tp == 1:
            t1.setPos(-505,-355)
            if acpt == 1:
                backgrounds.gbr(t5)
                dlp = dlp - 203
                if dlp < 0:
                    dlp = 0
                mp = 0
                t1.setPos(0,0)
                backgrounds.gb(t5)
                texts.aTe2(t5)
                delay(3000)
                backgrounds.gbr(t5)
                delay(1000)
        elif tp == 2:
            t1.setPos(-225,-355)
            if acpt == 1:
                backgrounds.gbr(t5)
                mp = 0
                damage = damage + 3
                t1.setPos(0,0)
                backgrounds.gb(t5)
                texts.actte(t5)
                delay(3000)
                backgrounds.gbr(t5)
                delay(1000)
        elif tp == 3:
            t1.setPos(65,-355)
            if acpt == 1:
                backgrounds.gbr(t5)
                lp = lp - 23
                mp = 0
                t1.setPos(0,0)
                backgrounds.gb(t5)
                texts.pizza(t5)
                delay(6000)
                backgrounds.gbr(t5)
                delay(1000)
        elif tp == 4:
            t1.setPos(345,-355)
            if acpt == 1:
                backgrounds.gbr(t5)
                mp = 0
                t1.setPos(0,0)            
                backgrounds.gb(t5)
                texts.spTe2(t5)
                delay(4000)
                backgrounds.gbr(t5)
                delay(1000)

#event-texte
def ate(pTurtle):
    global dlp
    pTurtle.setFontSize(32)
    pTurtle.setPenColor("white")
    pTurtle.setPos(300,355)
    pTurtle.label("*hit")
    pTurtle.setPos(300,315)
    pTurtle.setFontSize(32)
    pTurtle.setPenColor("yellow")
    pTurtle.setPos(300,155)
    teStr = str(dlp)
    pTurtle.label(teStr + " / 1000")


"gibt den Turtles Farben und erstellt sie"
t1 = makeTurtle(mouseMoved = onMouseMoved,keyPressed = onKeyPressed)
t1.setColor("red")
t1.speed(-1)
t2 = Turtle(t1)
t3 = Turtle(t1,"sprites/chesswhite_0.png")
t4 = Turtle(t1,"white")
t4.hideTurtle()
t5 = Turtle(t1)
t5.hideTurtle()
t6 = Turtle(t1,"white")
t6.hideTurtle()

lp1 = Turtle(t1)
lp1.hideTurtle()
lp1.setPos(-50,-200)
lp1.setPenColor("white")
lp1.setFontSize(32)


t2.setPos(600,400)
t2.hideTurtle()

t3.setPos(0,200)




#game

t5.setFillColor("gray")
t5.fill()
t5.setPenColor("red")
t5.setFontSize(100)
t5.setPos(-320,-150)
t5.label("Under May Tale")

lp = 0

plp = 42


t5.setPenColor("white")
t5.setPenWidth(8)
t5.setFontSize(36)

name = input("Input Name:")
if name == "Joschroe":
    msgDlg("Hey, that's my name, yk?!")
    lp = -420
else:
    msgDlg("Your name now is "+ name)
if name == "ghost":
    t1.hideTurtle()
    t1 = Turtle(t1,"sprites/ghost_1.gif")
elif name == "cbt":
    t1.hideTurtle()
    t1 = Turtle(t1,"sprites/dwarf0.png")
    lp = 69420
    clean("black")
    backgrounds.gb(t4)
    texts.cbt(t5)
    t1.setPenColor("white")
    t1.setFontSize(12)
    delay(1200)
    t1.label("ich bin nicht so klein!")
    delay(6000)
    clear("black")
    backgrounds.yKill(t4)
    end(t4)
    delay(69420)
elif name == "wertzu wuniri_123 kohlmann suppenkasper mag damaris fr fr":
    t1.hideTurtle()
    t1 = Turtle(t1,"sprites/elefant.gif")
    dlp = 100

clean("black")

backgrounds.fight(t2)
delay(800)

t5.setPos(-500,-250)
t5.label(name)

    
def attacksG():
    global dlp
    #anfang, phase 0
    backgrounds.gb(t5)
    texts.te1(t5)
    delay(3000)
    backgrounds.gbr(t5)
    
    "mp 1"
    mpp(t4)
    if dlp <= 0:
        backgrounds.bKill(t4)
        end(t4)
    else:
        #phase 1
        attacks.a1(t4)    
        t4.setPos(100,-100)
        attacks.a1(t4)
        t4.setPos(-100,100)
        attacks.a1(t4)
        delay(1000)
        #phase 2
        t4.setPos(0,-15)
        attacks.a2(t4)
        t4.setPos(-80,-15)
        attacks.a2(t4)
        t4.setPos(80,-15)
        attacks.a2(t4)
        delay(1000)
        #phase 3
        attacks.a3(t4)
        delay(1000)
        "mp 2"
        mpp(t4)
        if dlp <= 0:
            backgrounds.bKill(t4)
            end(t4)
        else:
            #phase 4
            attacks.a4(t4)
            delay(600)
            backgrounds.fight(t4)
            #phase 5
            attacks.a5(t4)
            "mp 3"
            mpp(t4)
            if dlp <= 0:
                backgrounds.bKill(t4)
                end(t4)
            else:
                #phase 6
                attacks.a6(t4)
                #phase 7
                attacks.a7(t4)
                #phase 5 v.2
                attacks.a5v2(t4)
                #phase 8
                attacks.a8(t4)
                "mp 4"
                mpp(t4)
                if dlp <= 0:
                    backgrounds.bKill(t4)
                    end(t4)
                else:
                    #phase 9
                    attacks.a8(t4)
                    t4.setPos(-100,-30)
                    attacks.a1(t4)
                    attacks.a3(t4)
                    attacks.a5v2(t4)
                    backgrounds.gb(t5)
                    
                    texts.finTe1(t5)
                    delay(4000)
                    backgrounds.gbr(t5)
                    
                    a9(t4)
                    
                    if dlp < 200:
                        delay(200)
                        backgrounds.fight(t4)
                        
                        texts.finTe2(t6)
                        delay(2000)
                        backgrounds.gbr(t6)
                        delay(80)
                        
                        texts.finTe3(t6)
                        delay(5000)
                        backgrounds.gbr(t6)
                        delay(80)
                        
                        texts.finTe8(t6)
                        delay(5000)
                        backgrounds.gbr(t6)
                        delay(80)
                        
                        texts.finTe4(t6)
                        delay(5000)
                        backgrounds.gbr(t6)
                        delay(80)
                        
                        texts.ppp(t6)
                        delay(2000)
                        backgrounds.gbr(t6)
                        
                        texts.finTe5(t6)
                        delay(4000)
                        backgrounds.gbr(t6)
                        delay(80)
                        
                        texts.ppp(t6)
                        delay(5000)
                        backgrounds.gbr(t6)
                        
                        texts.finTe6(t6)
                        delay(5000)
                        backgrounds.gbr(t6)
                        delay(80)
                        
                        texts.finTe7(t6)
                        delay(5000)
                        backgrounds.gbr(t6)
                        delay(80)
                        "mp 5"
                        mppE(t4)
                        if dlp == 0:
                            backgrounds.bKill(t4)
                        else:
                            a9e(t4)
                            backgrounds.yKill(t4)
                    else:
                        backgrounds.yKill(t4)
                        

#führt die Attacken aus    
attacksG()

#end-sequenz
clear("black")
if name == "Joschroe":
    t5.setFontSize(69)
    t5.setPos(0,0)
    t5.setPenColor("yellow")
    t5.label(lp)
    t5.setPos(120,50)
    t5.startPath()
    t5.setFillColor("black")
    delay(1000)
    clear("black")
    t5.setPenColor("green")
    t5.setPos(120,50)
    t5.setFontSize(69)
    t5.label("no skill")
    t5.setPos(50,-50)
    t5.setFontSize(26)
    t5.label("Never gonna give you up")
elif name == "ghost":
    lp = 0
    t5.setFontSize(69)
    t5.setPos(0,0)
    t5.setPenColor("yellow")
    t5.label(lp)
    t5.setPos(120,50)
    t5.startPath()
    t5.setFillColor("black")
    delay(1000)
    clear("black")
    t5.setPenColor("cyan")
    t5.setPos(120,50)
    t5.setFontSize(69)
    t5.label("Ghost Mode")
    t5.setPos(50,-50)
    t5.setFontSize(26)
    t5.label("No score")
else:
    end(t5)
