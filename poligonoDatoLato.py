import turtle
tartaruga = turtle.Turtle()
tartaruga.goto(00,300)
tartaruga.clear()
tartaruga.color('red', 'yellow')
tartaruga.begin_fill()
print("\n INSERIRE IL NUMERO DI Linserire numero dei lati")
nLati = int(input())
angolo = float(360 / nLati)
for temp in range(0,nLati):
    tartaruga.right(angolo)
    tartaruga.forward(1000/nLati)
tartaruga.end_fill()
