from funcoes import *


while True:
    Y = input("Digite o produto:")
    X = int(input("Digite o preco:"))

    ProdutoePreco(Y, X)

    sair = input("Deseja digitar novamente?\nS/N: ")
    if sair == "N":
        break
print(prod)
print(prec)
