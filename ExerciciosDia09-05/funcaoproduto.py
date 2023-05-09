def produtos(produto, quantidade, valorUni):
    return quantidade * valorUni


P = produtos("Fuba", 40, 3)
print(f"O valor total do estoque é {P}")
