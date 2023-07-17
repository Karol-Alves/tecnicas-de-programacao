v1 = float(input(f'Digite um valor: \n'))
v2 = float(input(f'Digite outro valor: \n'))
operador = str(input(f'Digite o operador +, - , * ou / : \n'))


if (operador == '+'):
    resultado = v1+v2
    print(f"O resultado é: {resultado}")

elif (operador == '-'):
    resultado = v1-v2
    print(f"O resultado é {resultado}")

elif (operador == '*'):
    resultado = v1*v2   
    print(f"O resultado é {resultado}")

elif (operador == '/'):
    resultado = v1/v2 
    print(f"O resultado é {resultado}")

else:
    print(f"Erro, digite um novo valor \n")