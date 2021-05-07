import pygame
import sys
from pygame import draw
from math import dist
from pygame.constants import QUIT
import time
posizioni = []
global posAttuale,possibilitaFuture,perimetro
perimetro = [[0,0,0,1,1],[1,0,0,0,1],[0,0,1,1,1],[0,0,1,0,0],[1,0,0,0,0],[1,1,1,0,0]]
DIMENSIONE_CASELLA = 50
DIMENSIONI = (DIMENSIONE_CASELLA * len(perimetro[0]),DIMENSIONE_CASELLA * len(perimetro))

BIANCO = (255,255,255)
NERO = (0,0,0)
ROSSO = (255,0,0)
VERDE = (0,255,0)


possibilitaFuture = {}

'''
class Robot(pygame.sprite.Sprite):
    widht = 20
    height = 20          
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)
       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface([width, height])
       self.image.fill(VERDE)
       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
'''

def faiPossibilità():
    global possibilitaFuture,posizioni
    possibilita = []
    global perimetro
    cnt = 0
        
    #assegna a ogni casella libera un numero
    for riga in range(len(perimetro)):
        for cella in range(len(perimetro[riga])):
            if(perimetro[riga][cella] == 0):
                perimetro[riga][cella] = cnt
                cnt+=1
            else:
                perimetro[riga][cella] = -1


    #riempieil dizionario con le prossime possibilità
    cnt = 0
    for riga in range(len(perimetro)):
        for cella in range(len(perimetro[riga])):
            possibilita = []
            if(perimetro[riga][cella]!=-1):
                    
                if(cella>=1):
                    if(perimetro[riga][cella-1]!=-1):
                        possibilita.insert(0,(perimetro[riga][cella-1],1))
                if(cella+1<len(perimetro[riga])):
                    if(perimetro[riga][cella+1]!=-1):
                        possibilita.insert(0,(perimetro[riga][cella+1],1))
                if(riga>=1):
                    if(perimetro[riga-1][cella]!=-1):
                        possibilita.insert(0,(perimetro[riga-1][cella],1))
                if(riga+1<len(perimetro)):
                    if(perimetro[riga+1][cella]!=-1):
                        possibilita.insert(0,(perimetro[riga+1][cella],1))
                
                if(len(possibilita) != 0):
                    posizioni.append((riga,cella))
                
                possibilitaFuture[cnt] = possibilita
                #possibilitaFuture[cnt].append((1)) #aggiunge peso
                cnt+=1






def drawPlayground():
    for y in range(len(perimetro)):
        for x in range(len(perimetro[0])):
            piastrella = pygame.Rect(x*DIMENSIONE_CASELLA,y*DIMENSIONE_CASELLA,DIMENSIONE_CASELLA,DIMENSIONE_CASELLA)
            if(perimetro[y][x] != -1):
                pygame.draw.rect(screen,BIANCO,piastrella)
            else:
                pygame.draw.rect(screen,ROSSO,piastrella)
                

def controllaMovimenti(event):
    global posAttuale 
    spostX = 0
    spostY = 0
    if event.key == pygame.K_w:
        spostY = -1
    elif event.key == pygame.K_a:
        spostX = -1
    elif event.key == pygame.K_s:
        spostY = 1
    elif event.key == pygame.K_d:
        spostX = 1

    for posFuture in possibilitaFuture[posAttuale]:
        if((posizioni[posAttuale][0] +spostY,posizioni[posAttuale][1]+spostX) == posizioni[posFuture[0]]):
            posAttuale = posFuture[0]

def posizioneAttuale():
    piastrella = pygame.Rect(posizioni[posAttuale][1]*DIMENSIONE_CASELLA,posizioni[posAttuale][0]*DIMENSIONE_CASELLA,DIMENSIONE_CASELLA,DIMENSIONE_CASELLA)
    pygame.draw.rect(screen,VERDE,piastrella)

def dijkstra(start,dizionario):
    label={}
    nodeList=[start]
    nodesEliminati=[]
    predecessori={}
    INF = 999999999
    for nodo in dizionario:
        label[nodo]=INF
        predecessori[nodo]=None

    label[start]=0

    while len(nodeList) > 0:
        #cerco tra i nodi presenti in nodelist quello che ha la label più piccola
        #il nodo trovato sarà il nodo corrente
        #print(nodeList)
        nodeCorr=nodeList[0]
        for node in nodeList:
            if label[node]<label[nodeCorr]:
                nodeCorr=node
        #print(f"il nodo corrente è: {nodeCorr}")
        #trovo le adiacenze a partire dal nodo corrente - FOR
        #per ogni adiacenza calcolo la nuova label aggiornando il dizionario label solo se la label trovata
        #risulta piu piccola di quella gia trovata - FOR
        for nodesAdjT in dizionario[nodeCorr]:
            if not(nodesAdjT[0] in nodesEliminati) and not(nodesAdjT[0] in nodeList):
                nodeList.append(nodesAdjT[0])
            if label[nodeCorr]+nodesAdjT[1] < label[nodesAdjT[0]]:
                label[nodesAdjT[0]]=label[nodeCorr]+nodesAdjT[1]
                predecessori[nodesAdjT[0]]=nodeCorr
        nodeList.remove(nodeCorr)
        nodesEliminati.append(nodeCorr)
    return label,predecessori

def vaiAllaPosizione():
    global posAttuale
    pos = pygame.mouse.get_pos()
    x = (int(pos[0]/DIMENSIONE_CASELLA))
    y = (int(pos[1]/DIMENSIONE_CASELLA))
    
    if((y,x) not in posizioni):
        return
    
    
    percorso = [posizioni.index((y,x))]
    
    while percorso[-1]!=posAttuale:
        percorso.append(predecessori[percorso[-1]])
    percorso.reverse()
    
    
    for step in percorso:
        posAttuale = step 
        drawPlayground()
        posizioneAttuale()
        pygame.display.update()
        time.sleep(0.5)



distanze = []
predecessori = None
def main():
    
    global screen,possibilitaFuture,posAttuale,distanze,predecessori
    pygame.init()
    screen = pygame.display.set_mode(DIMENSIONI)
    screen.fill(NERO)

    faiPossibilità()
    posAttuale = 0
    #a  = Robot(VERDE,200,200)
    
    while True:
        drawPlayground()
        posizioneAttuale()
        pygame.display.update()
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                controllaMovimenti(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                distanze,predecessori = dijkstra(posAttuale,possibilitaFuture)
                vaiAllaPosizione()
                



if(__name__ == "__main__"):
    main()
