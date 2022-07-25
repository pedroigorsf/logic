salario = int(input("Digite o valor do seu salário: "))

if salario < 500:
  print("\nSeu salário atual é {} e passará a ser {} por conta do reajuste de 15%.".format(salario,(salario*0.15)+salario))
elif salario >= 500 and salario <= 1000:
  print("\nSeu salário atual é {} e passará a ser {} por conta do reajuste de 10%.".format(salario,(salario*0.10)+salario))
elif salario > 1000:
  print("\nSeu salário atual é {} e passará a ser {} por conta do reajuste de 5%.".format(salario,(salario*0.05)+salario))
else:
  print("\nO valor digitado está errado.");
