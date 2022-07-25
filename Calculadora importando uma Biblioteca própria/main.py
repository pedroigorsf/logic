import calculadora as calc

v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("Digite o primeiro valor: "))

escolha = int(input("""
....:::: Calculadora :::::....
1) Somar
2) Subtrair
3) Multiplicar
4) Dividir

Escolha uma das opções acima: """))

if escolha == 1:
  calc.soma(v1,v2)

elif escolha == 2:
  calc.sub(v1,v2)

elif escolha == 3:
  calc.mult(v1,v2)

elif escolha == 4:
  calc.div(v1,v2)

else: print("O valor digitado é inválido.")

