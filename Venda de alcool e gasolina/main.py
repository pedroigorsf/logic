
precogasolina = 2.50
precoalcool = 1.90
#gasolina R$ 2,50
#alcool R$ 1,90

escolha = int(input("O que deseja?\n\n 1 - Gasolina\n 2 - Alcool\n\nEscolha uma das opções acima."))

litro = int(input("\nQuantos litros? "))

#GASOLINA
#até 20 - 3%
#mais de 20 - 5%
if escolha == 1 and litro <= 20:    #GASOLINA
  print("\nLitros: {}\nGasolina: R$ {}\nTotal: R$ {}\nDesconto: R$ {}\n\nObs.: Até 20 litros de Gasolina tem 3% de desconto.".format(litro, precogasolina, precogasolina*litro, (precogasolina*litro)*0.03))
if escolha == 1 and litro > 20:    #GASOLINA
  print("\nLitros: {}\nGasolina: R$ {}\nTotal: R$ {}\nDesconto: R$ {}\n\nObs.: Acima de 20 litros de Gasolina tem 5% de desconto.".format(litro, precogasolina, precogasolina*litro, (precogasolina*litro)*0.05))


#ALCOOL
#até 20 - 4%
#mais de 20 - 6%
if escolha == 2 and litro <= 20:    #ALCOOL
  print("\nLitros: {}\nAlcool: R$ {}\nTotal: R$ {}\nDesconto: R$ {}\n\nObs.: Até 20 litros de Alcool tem 4% de desconto.".format(litro, precoalcool, precoalcool*litro, (precoalcool*litro)*0.04))
if escolha == 2 and litro > 20:    #ALCOOL
  print("\nLitros: {}\nAlcool: R$ {}\nTotal: R$ {}\nDesconto: R$ {}\n\nObs.: Acima de 20 litros de Alcool tem 6% de desconto.".format(litro,precoalcool, precoalcool*litro, (precoalcool*litro)*0.06))