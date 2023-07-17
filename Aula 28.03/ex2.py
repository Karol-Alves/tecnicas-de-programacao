produto = input(f"Digite o produto: \n")
valor = float (input(f"Digite o valor da compra: \n"))

if valor < 10 :
    venda= valor + (valor*0.7)
    print(f"Produto: {produto}\n Venda: {venda}")
elif valor >= 10 and valor < 30:
    venda= valor + (valor*0.5)
    print(f"Produto: {produto}\n Venda: {venda}")
elif valor >= 30 and valor < 50:
    venda= valor + (valor*0.4)
    print(f"Produto: {produto}\n Venda: {venda}")
else:
    venda= valor + (valor*0.3)
    print(f"Produto: {produto} \n Venda: {venda}")
