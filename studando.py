# maior_numero = -9999999999

# numero = int(input("digite o seu numero , ou digite -1 para sair: "))
# while numero != -1:
#     if numero > maior_numero:
#         maior_numero = numero
#     numero = int(input("digite o seu numero , ou digite -1 para sair: "))

# print("o maior numero é: ",maior_numero)

import os
os.system('cls')

numero_secreto = 777

print("+"+"="*21+"+")
print("|"+"bem vindo ao meu jogo"+"|")
print("|"+"voce esta preso aqui"+" "+"|")
print("|"+"ate acertar o numero"+" "+"|")
print("|"+"ultra secreto :P"+"     "+"|")
print("+"+"="*21+"+")
chute = int(input("\ndigite aqui o seu chute: "))

while chute != numero_secreto:
    print("VOCE ESTA PRESO ATE ACERTAR")
    chute2 = int(input("\nTENTE NOVAMENTE: "))
    chute = chute2
if chute == numero_secreto:
    print("\ndroga :(\nvoce acertou:P")


    