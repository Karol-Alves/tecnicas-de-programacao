num = int(input("digite um numero com tres digitos:"))
d1= num // 100
d2= num % 100//10
d3= num % 10
inverso=d3*100+d2*10+d1
print("o inverso do numero digitado e:" ,inverso)