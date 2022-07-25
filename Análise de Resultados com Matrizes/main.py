

matriz = [["Gol","Fusca","Vectra"],[ 13.6, 10.7, 7.4]]

for x in range(2):
  for y in range(3):
    if matriz[x][y] == "Gol":
      print(matriz[x][y])
      print(matriz[x+1][y])
    elif matriz[x][y] == "Fusca":
      print(matriz[x][y])
      print(matriz[x+1][y])
    elif matriz[x][y] == "Vectra":
      print(matriz[x][y])
      print(matriz[x+1][y])


maior = matriz[1][0] # MAIOR KM por Litro
carro = matriz[0][0] # Carro

if matriz[1][1] > maior:
  maior = matriz[1][1]
  carro = matriz[0][1]
if matriz[1][2] > maior:
  maior = matriz[1][2]
  carro = matriz[0][2]


print("\n O ",carro," é mais económico e faz ",maior," km/l")
