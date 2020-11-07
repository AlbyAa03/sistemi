import random
vet = [0]

vet[0] = int ((random.random()*100)  / 1)
for num in range(0,10):
    vet.append(int (random.random()*100)  / 1)


for numeri in vet:
     print(numeri)


def bubbleSort(vet, nums):
    for numeri in range(nums):
        for scambio in range(nums):
            if(vet[scambio]<vet[scambio+1]):
                vet[scambio],vet[scambio+1] = vet[scambio+1],vet[scambio]

bubbleSort(vet,10)
print("-------------")
for numeri in vet:
    print(numeri)