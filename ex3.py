valor = float (input(f"Digite o valor da compra \n"))
if valor >= 200 :
    valor = valor-(valor * 0.2)
    print(f"Sua compra com 20% de desconto é ${valor}")
else:
    print(f"O valor da sua compra é ${valor}")