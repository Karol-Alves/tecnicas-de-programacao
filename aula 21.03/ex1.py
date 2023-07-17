"""Faça um programa em Python que calcule e mostre o valor do volume do tronco de uma pirâmide, para isso o programa deve solicitar ao usuário os valores da altura do tronco da pirâmide (h), o valor da base menor (Bmenor) e o da base maior (Bmaior) e calcular a seguinte expressão:
 volume =h/3*(Bmaior**2 +  Bmenor**2 + (Bmaior**2 * Bmenor**2)**0.5)"""
h= float(input(f"Digite a altura do tronco da piramide: \n"))
bMenor=float(input(f"Digite o valor da base menor: \n"))
bMaior= float(input(f"Digite o valor da base maior: \n"))

volume= h/3*(bMaior**2 + bMenor**2 + (bMaior**2 * bMenor**2)**0.5)

print("O resultado da formula e:" ,volume)
