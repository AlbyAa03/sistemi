'''
Il file annual.csv (allegato) contiene la anomalia della temperatura globale del pianeta Terra dal 1880 ad oggi, 
proveniente da varie fonti (colonna “Source”).
Scrivere un programma che generi un dizionario che abbia come chiave l’anno (“Year”) 
e valore la media aritmetica delle anomalie registrate dalle varie fonti durante quell’anno.
Inoltre scrivere una funzione che dati in input due anni diversi (anno_1 e anno_2) 
trovi la anomali massima e minima nel periodo compreso tra anno_1 e anno_2.

Source,Year,Mean

'''
def anomaliaMassimaMinima(diz,anno1,anno2): #passa il dizionario e 2 anni
    massima = diz[str(anno1)]#massima e minima hanno inizialmente valori del primo anno passato
    minima = diz[str(anno1)]
    for anno in diz: # cicla tutta la lista
        #se appartiene al range anno1<=x<=anno2 o anno2<=x<=anno1
        if((int(anno) >= anno1  and int(anno)<=anno2) or (int(anno) <= anno1  and int(anno) >= anno2)): # la or serve se l'utente intendeva cercare dal secondo numero al primo
            if(massima<diz[anno]):#se la massima attuale è minore del valore dell'anno corrente
                massima = diz[anno] #massima = al valore dell'anno attuale
            elif(minima>diz[anno]):#else-if è maggiore di quella minima(so che se prima era vero, di sicuro non sarà quella minima)
                minima = diz[anno] #temperatura minima = temperatura attuale
    print("massimo: "+str(massima) +". Minimo: "+ str(minima)) # stampa valori massimo e minimo

if __name__ == "__main__":
    file = open("./annual.csv",'r')
    cnt = 0
    temp = 0
    anni = {}
    for riga in file: # legge il file
        try: # prova a leggere la riga e compararla a numeri float
            if (cnt%2 == 0): # se si sta guardando una riga pari (serve per fare la media dei numeri su più righe)
                temp = float(riga.split(',')[2]) # si salva il valore della temperatura in una variabile temporale
            else:# se si sta leggendo una riga dispari
                anni[riga.split(',')[1]] = (float(temp) + float(riga.split(',')[2]) )/2# salva in un dizionario la media di un anno sotto il nome dell'anno corrente
            cnt = (cnt+1)%2# cnt può assumere valori 0 o 1
        except: pass # se non ci riesce non fa niente ( pass visto due lezioni fa e except su un video tutorial)
            

    for elemento in anni: # serve più che altro a me per vedere se ha salvato correttamente tutte le temperature
        print( elemento + " "+str(anni[elemento]))         

    anomaliaMassimaMinima(anni,2009,20015) #stampa valori massimo e minimo tra due date

    file.close()# chiude il file
