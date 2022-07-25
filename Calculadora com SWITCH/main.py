valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

escolha = float(input("\nDigite um número de 1 a 4: \n1 - Adição (+)\n2 - Subtração (-)\n3 - Multiplicação (*)\n4 - Divição (/)\n\nEscolha uma das opções acima."))

if escolha == 1:
  print("\nA soma de",valor1,"+",valor2,"é igual a: ",valor1+valor2)
elif escolha == 2:
  print("\nA subtração de",valor1,"-",valor2,"é igual a: ",valor1-valor2)
elif escolha == 3:
  print("\nA multiplicação de ",valor1,"*",valor2,"é igual a: ",valor1*valor2)
elif escolha == 4:
  if valor2 == 0:
    print("\nImpossível dividir por zero")
  else:
    print("\nA divisão de",valor1,"/",valor2,"é igual a: ",valor1/valor2)
else:
  print("\nO valor digitado está diferente do solicitado.");
