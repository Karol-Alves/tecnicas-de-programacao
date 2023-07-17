idade= int(input(f"Digite sua idade: \n"))

if idade < 16:
    print("Não eleitor")
elif idade >= 18 and idade <= 65:
    print("Eleitor obrigatório")
else :
    print("Eleitor facultativo")