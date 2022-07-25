tentativas = 9

for x in range(10): #10 tentativas
  senha = int(input("Digite o digito secreto: "))
  if senha == 7:
    print("\nBem vindo(a)!")
    break;
  print("\nErrado! Você ainda tem ",tentativas," tentativas")
  tentativas -= 1
if tentativas == 0:
  print("\nSistema bloqueado!")