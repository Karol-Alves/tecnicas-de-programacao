num = int(input("Quantas pessoas?"))
alturaMulher = 0
alturaHomem = 0
quantidadeMulheres = 0
quantidadeHomens = 0
for i in range(num):
    sx = input("Digite o sexo da pessoa {}: ".format(i+1))
    alt = float(input("Agora, digite sua altura em metros {}: ".format(i+1)))
    if sx.upper() == 'F':
        alturaMulher += alt
        quantidadeMulheres += 1
    elif sx.upper() == 'M':
        alturaHomem += alt
        quantidadeHomens += 1
if quantidadeMulheres > 0:
    media_m = alturaMulher / quantidadeMulheres
    print("A média de altura de mulheres é {:.2f} metros".format(media_m))
else:
    print("Não há mulheres.")
if quantidadeHomens > 0:
    media_h = alturaHomem / quantidadeHomens
    print("A média de altura de homens é {:.2f} metros".format(media_h))
else:
    print("Não há homens.")