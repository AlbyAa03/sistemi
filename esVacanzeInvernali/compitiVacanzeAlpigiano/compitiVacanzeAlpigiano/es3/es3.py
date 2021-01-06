'''
Nella serie di Fibonacci, ciascun numero della serie è la somma dei due numeri nella serie che lo precedono, ad esempio:
1, 1, 2, 3, 5, 8, 13 (...)
Scrivi una funzione ricorsiva che restituisce in output i numeri della sequenza di Fibonacci, entro una soglia specifica impostata dall'utente.
'''

def inputNum(): #input numero positivo (ricorsivo)
    print("Inserire un numero INTERO POSITIVO")
    n = int(input()) #dovrei usare una try-except, ma non ce lo so ancora usare bene
    if(n < 0): # se il numero è negativo richiama se stessa
        n = inputNum() #sarebbe come un do-while, fa il controllo alla fine e se è vero allora ritorna da capo
    return n #returna l'input

def fibonacci(n1,n2,cnt):# gli passo il penultimo numero, l'ultimo e quanti numeri devo ancora stampare
    n3=n1+n2 #sommo i due valori passati e lo assegno a n3
    if(n3 == 0): n3 = 1    #se la somma è 0 allora assegno a 'n3' 1
    if(cnt>0): # se deve ancora stampare numeri
        print(n3, end=" ") # stampa la somma dei numeri passati (n3)
        fibonacci(n2,n3,cnt-1) # gli passo l'ultimo numero, la somma dell'ultimo con il penultimo e quanti numeri deve ancora stampare

if __name__ == "__main__":
    lung = inputNum() # prende in input un numero intero positivo
    fibonacci(0,0,lung) # stampa la serie di fibonacci

