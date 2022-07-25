valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

if valor1 > valor2:
  print("\nO valor {} é maior que o valor {}".format(valor1,valor2))
elif valor2 > valor1:
  print("\nO valor {} é maior que o valor {}".format(valor2,valor1))
else:
  print("\nO valor {} e {} são iguais".format(valor1,valor2))
