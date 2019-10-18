from random import randint
from time import sleep
itens=('predra', 'papel', 'tesoura')
computador=randint(0, 2)
print('\033[36m'+'''SUAS OPÇÕES: 
[0]PEDRA 
[1]PAPEL 
[2]TESOURA'''+'\033[0;0m')
jogador=int(input('\033[36m'+'FAÇA SUA JOGADA! '+'\033[0;0m'))
print('\033[31m'+'-=' * 33 +'\033[0;0m')
print('\033[36m'+'JO'+'\033[0;0m')
sleep(1)
print('\033[36m'+'KEN'+'\033[0;0m')
sleep(1)
print('\033[36m'+'PÔ!!!'+'\033[0;0m')
print('\033[31m'+'-=' * 33 +'\033[0;0m')
print('\033[36m'+'Computador jogou {}'.format(itens[computador]+'\033[0;0m'))
print('\033[36m'+'Você jogou {}'.format(itens[jogador]+'\033[0;0m'))
print('\033[31m'+'-=' * 33 +'\033[0;0m')
if computador==0:
    if jogador==0:
        print('\033[36m'+'DEU EMPATE! '+'\033[0;0m')
    elif jogador==1:
        print('\033[36m'+'VOCÊ VENCEU! '+'\033[0;0m')
    elif jogador==2:
        print('\033[36m'+'O COMPUTADOR VENCEU! '+'\033[0;0m')
    else:
        print('\033[36m'+'JOGADA INVALIDA! '+'\033[0;0m')
elif computador==1:
    if jogador==0:
        print('\033[36m'+'COMPUTADOR VENCEU! '+'\033[0;0m')
    elif jogador==1:
        print('\033[36m'+'DEU EMPATE! '+'\033[0;0m')
    elif jogador==2:
        print('\033[36m'+'VOCÊ VENCEU! '+'\033[0;0m')
    else:
        print('\033[36m'+'JOGADA INVALIDA! '+'\033[0;0m')
elif computador==2:
    if jogador==0:
        print('\033[36m'+'VOCÊ VENCEU! '+'\033[0,0m')
    elif jogador==1:
        print('\033[36m'+'O COMPUTADOR VENCEU! '+'\033[0,0m')
    elif jogador==2:
        print('\033[36m'+'DEU EMPATE! '+'\033[0;0m')
    else:
        print('\033[36m'+'JOGADA INVALIDA! '+'\033[0;0m')