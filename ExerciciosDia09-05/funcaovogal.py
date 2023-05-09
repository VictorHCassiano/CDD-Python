def vogal(frase):
    cont = 0
    for x in frase:
        if x in "aeiouAEIOU":
            cont += 1

    print(f"O numero de vogais é {cont}")
vogal("O rato roeu a roupa do rei de Roma")