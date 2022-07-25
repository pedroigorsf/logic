contador = 5

while contador != 0:
  login = int(input("login:  "))
  senha = int(input("senha:  "))
  if login == 123 and senha == 456:
    print("\nBem vindo(a)")
    break
  else:
    print("login/senha incorreto.")
  contador = contador - 1

if contador == 0:
  print("\nSistema bloqueado.")

