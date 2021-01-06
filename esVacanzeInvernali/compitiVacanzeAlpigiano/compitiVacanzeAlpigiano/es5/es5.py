'''
Implementare il videogioco snake tramite il modulo turtle.
'''
import turtle
import random
global snake,win,spostX,spostY,melaX,melaY,velAttuale,punteggio,turtlePunteggio,punteggioPrec  #inizializzazione di tutte le variabili globali

def settaVariabili(): # setta tutti i valori delle variabili globali
    global snake,win,spostX,spostY,melaX,melaY,velAttuale,punteggio,turtlePunteggio,punteggioPrec
    punteggioPrec = -1 # serve a stampare il punteggio ( se è diverso da quello attuale allora cancella il precedente, stampa quello attuale e mette questa variabile uguale a punteggio)
    punteggio = 0# punteggio attuale, viene incrementato ogni volta che si mangia una mela
    velAttuale = 0.5 #velocità dello snake. viene moltiplicato ad 1 o 0 per ogni coordinata, Sommato alla posizione attuale si ottiene la prossima posizione dello snake 
    snake = turtle.Turtle()# istanza della classe.Turtle turtle con nome snake. è lo snake vero e proprio
    win = turtle.Screen()# istanza della classe.Screen turtle con nome win
    spostX=1 # contiene lo spostamento sull'asse x. può assumere valori 0, 1 ,-1 ( in base al pulsante premuto)
    spostY=0# contiene lo spostamento sull'asse y. può assumere valori 0, 1 ,-1 ( in base al pulsante premuto)
    melaX = 20 # coordinata x della mela ( la prima mela viene sempre posizionata in [20,20])
    melaY = 20 # coordinata y della mela 
    turtlePunteggio = turtle.Turtle() # istanza della classe.Turtle turtle con nome turtlePunteggio. Mi è servita per stampare il punteggio
    turtlePunteggio.pencolor('white') #tolgo la colorazione a turtlePunteggio dello schermo in caso di spostamento
    turtlePunteggio.hideturtle() #nascondo la "freccina" di turtlePunteggio
    turtlePunteggio.goto(0,120) #sposto turtlePunteggio in (0,120)
    turtlePunteggio.pencolor('black') #tolgo la colorazione a turtlePunteggio dello schermo in caso di spostamento ( mi servirà poi per scrivere la scritta del punteggio)
    
def disegnaQuadrato():
    #disegna un quadrato di lato 200, disegnando e spostando di 80 gradi
    global snake,velAttuale
    snake.color('white')#togle il colore allo spostamento, perchè sennò c'è una linea che dal centro al lato del quadrato 
    snake.speed(0)#velocitè più grande che può assumere allo spostamento, almeno il quadrato non ci dovrebbe mettere tempo a disegnare ( velocità che riesce a elaborare il processore)
    snake.forward(100)
    snake.color('black') # rimetto il colore, sennò non disegna il quadrato
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
    snake.color('white')#togle il colore allo spostamento, perchè sennò c'è una linea che dal centro al lato del quadrato 
    snake.forward(100)
    snake.color('black')# rimetto il colore
    snake.left(180)#lo sposto che guarda verso destra
    snake.speed(velAttuale)#velocità 0.25 all'inizio
    

def disegnaMela(x,y):#disegna una mela(cerchio) in coordinate x,y passate per valore
    snake.speed(0) #velocità piu grande possibile allo snake
    pos = turtle.position() #si salva le posizioni attuali
    snake.setpos(x,y) #va nella posizione del cerchio ( centro)
    snake.pencolor('black') #disegna di nero
    snake.circle(3) # fa un cerchio nero di raggio 3
    snake.pencolor('white') # non può più disegnare
    snake.setpos(pos[0],pos[1]) # ritorna nelle posizioni che si era salvato
    #la velocità ritorna normale in haMangiato()

def cancellaMela(x,y): # cancella la mela(cerchio) in coordinate x,y passate per valore ( disegnando sopra un altro cerchio bianco)
    snake.speed(0) #posizione più grande possibile
    pos = turtle.position() # si salva le coordinate attuali
    snake.setpos(x,y) # va in posizione del cerhio da cancellare
    snake.circle(3) #disegna un cerchio bianco di raggio 3
    snake.setpos(pos[0],pos[1]) # ritorna nelle coordinate salvate precedentemente

def scriviPunteggio(): 
    global punteggio,turtlePunteggio,punteggioPrec
    if(punteggioPrec != punteggio): # se il punteggio attuale è diverso da quello precendente (è cambiato), serve a non riscrivere ad ogni ciclo di "principale()" il punteggio, rallentando di molto il programma 
        turtlePunteggio.clear()# cancella la scritta precedente
        turtlePunteggio.write('punteggio: '+ str(punteggio),align='center') # stampa il nuovo punteggio
        punteggioPrec = punteggio # assegna al punteggio precedente il punteggio attuale


def haMangiato(posX,posY): #controlla se ha "colliso" con il cerchio e se ha colliso cancella quello precedente e ne disegna uno nuovo in coordinate random
    global melaX,melaY,velAttuale,punteggio 

    if(abs(posX-melaX)<5 and abs(posY-melaY)<5):# controlla se le posizioni dello snake attuali sono interne alla mela. 5 perchè copre la maggior parte della circonferenza (vedi spiegazione alla riga successiva)
        #!! PERFEZIONABILE LA IF, perchè non controlla se è dentro la circonferenza, ma di un quadrato  di diagonale 10 con vertici verticali e orizzontali  
        # MA non ho voluto mettere la formula giusta perchè rallenterebbe troppo ogni volta fare seno e coseno e molitplicarli per il raggio 
        cancellaMela(melaX,melaY) #cancella mela 
        melaX = random.randint(-96,96) # tira fuori due coordinate in modo che il raggio non collida con il lato del quadrato e se le salva in variabili globali
        melaY = random.randint(-96,96)
        disegnaMela(melaX,melaY) # disegna una mela nelle nuove coordinate
        velAttuale += 0.5 # incermenta la velocità dello snake
        punteggio +=1 # incremenata punteggio

# funzioni che vengono richiamat  quando si preme da tastiera "wasd", modificando lo spostamento x e y. 
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

def principale(): #funzione che viene richiamata ogni 0 millisecondi all'inizio da se stessa
    scriviPunteggio() # scrive il punteggio 
    attuale=snake.position() #salva le coordinate attuali
    attualeX=attuale[0] # assegna ad altre variabili temporali le coordinate appena salvate
    attualeY=attuale[1]
    attualeX += spostX*velAttuale # incrementa la coordinata salvata con lo spostamento (in base a input da tastiera) e lo moltiplica alla velocità attuale, così da spostarsi in base alla valocità
    attualeY += spostY*velAttuale
    #P.S. non sposto lo snake con velAttuale in base al tempo per percorrere un determinato pezzo, MA IL CONTRARIO, lo spostamento che deve fare in un determinato tempo   
    haMangiato(attualeX,attualeY) #chiede se ha mangiato e disegna e cancella mele
    snake.setpos(attualeX,attualeY) # sposta lo snake nella nuova posizione calcolata 
    if(abs(attualeX)>=100 or abs(attualeY)>=100): # se esce dal cerchio termina il programma
        exit()
    win.ontimer(principale,0) # richiama la funzione 'principale()' fra 0 millisecondi


settaVariabili() # setta tutte le variabili con i valori iniziali
disegnaQuadrato() # disegna il quadrato esterno
disegnaMela(melaX,melaY) # disegn la prima mela

#funzioni che vengono chiamati ogni volta che si preme w,s,a,d  ( per cambiare direzioni)
win.onkeypress(up,"w")  
win.onkeypress(down,"s")
win.onkeypress(left,"a")
win.onkeypress(right,"d")

win.ontimer(principale,1)#chiama la principale fra 0 millisecondi
win.listen() # abilita gli input, quindi rende 'possibili' le funzioni "onkeypressed"  
win.mainloop()#inizia gli eventi turtle (win)