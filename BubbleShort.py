import random
'''
il mio programma....
'''

def bubbleSort(vet):
    nums=len(vet)
    for numeri in range(nums):
        for scambio in range(nums):
            if(vet[scambio]<vet[scambio+1]):
                vet[scambio],vet[scambio+1] = vet[scambio+1],vet[scambio]

vet=[] #lista vuota
for num in range(0,10):
    vet.append(random.randint(0,100))
print(vet)
bubbleSort(vet)
print("-------------")
print(vet)
