'''
Scrivi una funzione generatrice di password. La funzione deve generare una stringa alfanumerica di 8 caratteri qualora l'utente voglia una password semplice, o di 20 caratteri ascii qualora desideri una password più complicata.
'''
import random
import string
def inputLung(): # input di lunghezza che si richiama fino a quano non inserisce 8 o 20 ( più o meno è ricorsiva)
    print("parola semplice (inserire 8) o complicata (inserire 20)")# stampa messaggio di input
    n = int(input()) 
    if(n != 8 and n!=20): # se l'input è diverso da 8 e da 20
        n = inputLung() #sarebbe come un do-while, fa il controllo alla fine e se è vero allora ritorna da capo
    return n # returna l'input

if __name__ == "__main__":
    lung = inputLung() # assegna a lung 8 o 20 ( in base ad input da utente)
    parola = "" # inizializza una nuova parola
    possibilità = string.ascii_letters+string.digits # assgna a possibilità una stringa che va dalla A alla z più tutti i numeri decimali
    for _ in range(lung):#cicla da 0 a lung, non salvando il numero attuale (_), perchè tanto non lo uso
        lettera = random.choice(possibilità)#assegna a una variabile temporale un carattere a caso di "possibilità"
        parola += str(lettera) # aggiunge alla fine della parola la lettera random appena "estratta"
    print(parola) # scrive la parola creata