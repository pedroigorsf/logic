#------------------------------------#
# import os traz informações sobre o #
# sistema operacional (via terminal).#
#------------------------------------#
import os 
clear = lambda: os.system('clear')



#------------------------------------#
#      MENU FEITO USANDO while       #
#------------------------------------#
menuPrincipal=True
while menuPrincipal:
    
    print("""    _            _
   /_\    _  _  | |  __ _    
  / _ \  | || | | | / _` |   
 /_/ \_\  \_,_| |_| \__,_|   
  ___                            _     _      _
 |_ _|  _ _   __ __  ___   _ _  | |_  (_)  __| |  __ _ 
  | |  | ' \  \ V / / -_) | '_| |  _| | | / _` | / _` |
 |___| |_||_|  \_/  \___| |_|    \__| |_| \__,_| \__,_|
                                             

    1 - Consultar informações
    2 - Sair
    """)
    menuPrincipal=input("Escolha uma das opções (1 até 2):  ")


#--------------------------------------#
# Condição de seleção do MENU em while #
#--------------------------------------#
    if menuPrincipal=="1":
      clear() # Função do "import os"

#-----------------------------------------#
# A variável "idAluno" fica responsável   #
# por procurar as informações dentro dos  #
# arquivos "classe.txt" e "notas".        #
#-----------------------------------------#
      idAluno = input("""Qual aluno deseja pesquisar?
      

  1) Quico   
  2) Jaiminho
  3) Jirafales
  4) Nhonho

(Digite apenas números de 1 à 4)   """)
      
      clear()
#----------------------------------------------------#
# o FOR está lendo linha por linha o "classe.txt"    #
# o IF está procurando em cada linha o valor o       #
# valor da variável "idAluno", assim que achar       #
# irá printa apenas a linha do arquivo "classe.txt"  #
#----------------------------------------------------#
      print("___________ALUNO___________")
      print("ID | Nome")
      for linha in open('classe.txt'):
        if idAluno in linha:
          print(linha)
          break
#----------------------------------------------------#
# A informação se repete para o arquivo "notas.txt"  #
#----------------------------------------------------#
      print("___________NOTAS___________ ")
      print("ID | Av1 | Av2 | Av3 | Av4 |")
      
      for linha in open('notas.txt'):
        if idAluno in linha:
          print(linha)
          break
      else:
        clear()
#----------------------------------------------------#
# condição "else" caso o resultado não esteja válido #
#----------------------------------------------------#
        print("\n\nO valor digitado é invalido!")
#----------------------------------------------------#
# A condição "2" do MENU é responsável por encerrar  #
#----------------------------------------------------#
    elif menuPrincipal=="2":
      clear()
      print("\n Você foi deslogado do sistema.") 
      break;
    else:
#------------------------------------#
# Caso os valores de entrada sejam   #
# diferentes de "1" e "2" será       #
# apresentado uma mensagem de erro   #
#------------------------------------#
       clear()
       print("\n O valor digitado é invalido, favor, tente novamente!")
      