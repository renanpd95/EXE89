import os

n = 1
cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0
nul5 = 0
bran6 = 0


while (n > 0):
  os.system('clear')
  print("***************ELEIÇÃO PRESIDENCIAL********************")
  print("Escolha uma das opções de voto")
  print("1 --> Bolsonaro")
  print("2 --> Dilma")
  print("3 --> Lula")
  print("4 --> Maluf")
  print("5 --> Voto Nulo")
  print("6 --> Voto em Branco")
  opc = int(input("Digite a opção desejada: "))
  contin = str(input("Deseja continuar a votação (S/N): "))
  if(contin == "N" or contin == "n" or contin == "não" or contin == "NÃO"):
    n=0
    os.system('clear')
  
  if(opc == 1):
    cand1 = cand1 + 1
  elif(opc == 2):
    cand2 = cand2 + 1
  elif(opc == 3):
    cand3 = cand3 + 1
  elif(opc == 4):
    cand4 = cand4 + 1
  elif(opc == 5):
    nul5 = nul5 + 1
  elif(opc == 6):
    bran6 = bran6 + 1

else:
  print("****TOTAL DE VOTOS DOS CANDIDATOS*****")
  print("BOLSONARO ",cand1," VOTOS")
  print("LULA ",cand2," VOTOS")
  print("MALUF ",cand3," VOTOS")
  print("DILMA ",cand4," VOTOS")
  print("NULO ",nul5," VOTOS")
  print("BRANCO ",bran6," VOTOS")
  