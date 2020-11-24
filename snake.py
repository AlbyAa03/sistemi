import turtle

def disegnaQuadrato():
    global snake
    snake.forward(100)
    snake.left(90)
    snake.forward(100)
    snake.left(90)
    snake.forward(200)
    snake.left(90)
    snake.forward(200)
    snake.left(90)
    snake.forward(200)
    snake.left(90)
    snake.forward(100)
    snake.left(90)
    snake.forward(100)
    snake.left(180)
    
    
    
    

global snake
snake = turtle.Turtle()
global win 
win = turtle.Screen()
global spostX
spostX=1
global spostY
spostY=0

disegnaQuadrato()

def up():
    global spostX
    spostX =0
    global spostY
    spostY=1

def down():
    global spostX
    spostX =0
    global spostY
    spostY=-1
    
def left():
    global spostX
    spostX =-1
    global spostY
    spostY=0
    
def right():
    global spostX
    spostX =1
    global spostY
    spostY=0
    
def niente():
    attuale=snake.position()
    attualeX=attuale[0]
    attualeY=attuale[1]
    attualeX += spostX
    attualeY += spostY
    snake.goto(attualeX,attualeY)
    if(abs(attualeX)>100 or abs(attualeY)>100):
        exit()
    win.ontimer(niente,10)
    

win.onkeypress(up,"w")   
win.onkeypress(down,"s")
win.onkeypress(left,"a")
win.onkeypress(right,"d")
win.ontimer(niente,1000)
win.listen()
win.mainloop()