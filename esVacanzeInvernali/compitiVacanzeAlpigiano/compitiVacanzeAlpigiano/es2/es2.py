'''
Un indirizzo MAC (Media Access Control address) è un indirizzo univoco associato dal produttore, a una NIC, composto da 6 coppie di cifre esadecimali separate da due punti.
Un esempio di MAC è 02:FF:A5:F2:55:12.
Scrivi una funzione genera_mac che generi degli indirizzi MAC pseudo casuali.

'''
import random
import string

def genera_mac():
    mac="" #inizializza una nuova stringa
    for _ in range(6): # for che va da 0 a 6
        temp = random.choice(string.hexdigits) + random.choice(string.hexdigits) # assegna ad una variabile temporale due caratteri random da 0 a F in esadecimale 
        mac += temp + ":" #aggiunge alla fine del mac le due cifre HEX più due punti
    return mac[0:-1] #returna il mac, toglemdp l'ultimo ':', quindi da 0 all'ultima lettera (-1)

if __name__ == "__main__":
    mac= genera_mac() #genera un mac e lo assegna a mac
    print(mac) #stampa un mac
    