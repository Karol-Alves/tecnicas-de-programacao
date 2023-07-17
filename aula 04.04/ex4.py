listaDeValores = []
n = int(input("Digite o número de valores a serem inseridos: "))
for i in range (n):
    valor = float(input(f"Digite o {i+1}º valor: "))
    listaDeValores.append(valor)

positivos = 0
negativos = 0
menorValor = listaDeValores[0] 

for valor in listaDeValores:
    if valor > 0:
        positivos += 1
    elif valor < 0:
        negativos += 1
    if valor < menorValor:
        menorValor = valor

print(f"valores positivos: {positivos}")
print(f"valores negativos: {negativos}")
print(f"menor valor: {menorValor}")
