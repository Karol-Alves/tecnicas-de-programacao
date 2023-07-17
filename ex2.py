turno= input(f"Digite seu turno de trabalho \n")
horas= float (input(f"Digite suas horas trabalhadas \n"))

if turno == "n":
    salario=45.00*horas
    print(f"Seu salario é ${salario}")
else:
    salario=37.50*horas
    print(f"Seu salario é ${salario}")