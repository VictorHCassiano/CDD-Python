def produtos(produto, quantidade, valorUni):
    return produto, quantidade * valorUni


def vogal(frase):
    cont = 0
    for x in frase:
        if x in "aeiouAEIOU":
            cont += 1


def somar(n1, n2):
    return n1 + n2


def subtrair(n1, n2):
    return n1 - n2


def multiplicar(n1, n2):
    return n1 * n2


def dividir(n1, n2):
    return n1 / n2


def piramide(n1):
    for x in range(1, n1 + 1):
        print(str(x) * x)


def piramide1aN(n1):
    for x in range(1, n1 + 1):
        for y in range(1, x + 1):
            print(y, end=" ")
        print()


def checkPosNegPNZ(n):
    if n > 0:
        return "P"
    elif n < 0:
        return "N"
    else:
        return "Z"


prod = []
prec = []


def ProdutoePreco(produto, preco):
    prod.append(produto)
    prec.append(preco)


def somar_tudo(*args):
    soma = 0

    for x in args:
        soma += x
    return soma


def texto_inverso(palavra):
    cont = 0
    palavra_inversa = ""
    for x in palavra:
        if x != " ":
            cont += 1
    for y in range(len(palavra)):
        palavra_inversa = palavra[y] + "" + palavra_inversa
    return cont, palavra_inversa


def tirar_repeticao(a):
    nova_lista = []
    for x in a:
        if x not in nova_lista:
            nova_lista.append(x)

    return nova_lista


def tirar_repeticaofuncao(a):
    return list(sorted(set(a)))


def numero_primo(n):
    for x in range(2, n):
        if n % x == 0:
            return f"{n} não e primo"
    if n != 1:
        return f"{n} é primo"
    return "1 não é primo"
