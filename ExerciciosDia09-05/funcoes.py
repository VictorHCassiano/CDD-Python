def somar(n1, n2):
    return(n1 + n2)


def subtrair(n1, n2):
    return(n1 - n2)


def multiplicar(n1, n2):
    return(n1 * n2)


def dividir(n1, n2):
    return(n1 / n2)


while True:
    escolha = int(input("O que deseja fazer?\n1-Somar\n2-Subtrair\n3-Multiplicar\n4-Dividir\n5-Sair\n"))
    while escolha>5:
        escolha = int(input("Escolha invalida:"))
    if escolha == 5:
        break
    n1 = int(input("Digite um numero:"))
    n2 = int(input("Digite um numero:"))

    if escolha == 1:
       print(somar(n1,n2))
    elif escolha == 2:
        print(subtrair(n1,n2))
    elif escolha == 3:
        print(multiplicar(n1, n2))
    elif escolha == 4:
        print(dividir(n1, n2))
