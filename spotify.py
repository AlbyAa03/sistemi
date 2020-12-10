import random
lettura = open("./spotify.csv")
listaCanzoni = []

for cnt,riga in enumerate(lettura) :
    listaCanzoni.append({"numero":riga[:-1].split(",")[0],"titolo":riga[:-1].split(",")[1],"autore":riga[:-1].split(",")[1]})
   
   
copiaLista=listaCanzoni    
random.shuffle(copiaLista)
for canzone in copiaLista:
    print("Titolo: "+ canzone["titolo"]+ ". Autore: " + canzone["autore"])

lettura.close()