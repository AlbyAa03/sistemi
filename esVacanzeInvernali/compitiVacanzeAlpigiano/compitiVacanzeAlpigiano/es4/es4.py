'''
Il ROT-15 è un semplice cifrario monoalfabetico, in cui ogni lettera del messaggio da cifrare viene sostituita con quella posta 15 posizioni più avanti nell'alfabeto.
Scrivi una semplice funzione in grado di criptare una stringa passata, o decriptarla se la stringa è già stata precedentemente codificata.
'''
import string

def codifica(stringa):
    codificata = ""
    for lettera in stringa:
        lettera = chr(ord(lettera)+15)
        if(lettera> 'z'):
            lettera = chr((ord(lettera)%122)+96)
            #lettera = chr(ord(lettera)-26) #stessa cosa
        codificata +=lettera
    return codificata

def decodifica(stringa):
    decodificata = ""
    for lettera in stringa:
        lettera = chr(ord(lettera) - 15 )
        if(lettera < 'a'):
            lettera = chr(ord(lettera) +26)
        decodificata += lettera
    return decodificata
        
    

if __name__ == "__main__":
    print("inserire una parola")
    parola = str(input())
    parola = codifica(parola)
    print(parola)
    parola = decodifica(parola)
    print(parola)
    