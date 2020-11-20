from turtle import *
goto(00,300)
clear()
color('red', 'yellow')
begin_fill()
print("\n INSERIRE IL NUMERO DI Linserire numero dei lati")
nLati = int(input())
angolo = float(360 / nLati)
for temp in range(0,nLati):
    right(angolo)
    forward(1000/nLati)
end_fill()
done()
