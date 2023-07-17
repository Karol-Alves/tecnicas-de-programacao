salario=float (input(f"Digite seu salário \n"))
agua=float (input(f"Digite o valor da conta de água \n"))
luz=float (input(f"Digite o valor da conta de luz \n"))
telefone=float(input(f"Digite o valor da conta de telefone \n"))

if salario >= (agua+luz+telefone) :
    resto = salario - (agua+luz+telefone)
    print(f"Irá sobrar do seu salario R$ ${resto}")
else:
    print("Salário insuficiente")