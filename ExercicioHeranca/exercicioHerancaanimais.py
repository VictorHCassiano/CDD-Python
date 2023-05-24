A = []
contador = 0
media = 0

for x in range(10):
    A.append(int(input("Digite um numero:")))

menor = A[0]
maior = A[0]

print(A)
N1 = int(input("Digite qual numero voce quer saber quantas vezes aparece:"))
for y in range(10):
    if N1 == A[y]:
        contador += 1

print("O numero", N1, "aparece", contador, "vezes")
print("Os numeros pares são:")
for z in range(10):
    if A[z] % 2 == 0:
        print(A[z])

for x in range(10):
    if menor > A[x]:
        menor = A[x]
    if maior < A[x]:
        maior = A[x]

    media += A[x]
print("Maior:", maior, "Menor:", menor)
print("A média é", media/10)
print("Os numeros maiores que a media são:")
for i in range(10):
    if A[i] > media/10:
        print(A[i], end=" ")