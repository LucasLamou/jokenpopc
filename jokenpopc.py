from random import randint
from time import sleep
itens=('predra', 'papel', 'tesoura')
computador=randint(0, 2)
print('o computador escolheu{}'.format(itens[computador]))
print('''SUAS OPÇÕES: 
[0]PEDRA
[1]PAPEL
[2]TESOURA''')
jogador=int(input('FAÇA SUA JOGADA! '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!! ')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Você jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador==0:
    if jogador==0:
        print('DEU EMPATE! ')
    elif jogador==1:
        print('O VOCÊ VENCEU! ')
    elif jogador==2:
        print('O COMPUTADOR VENCEU! ')
    else:
        print('JOGADA INVALIDA! ')
elif computador==1:
    if jogador==0:
        print('O COMPUTADOR VENCEU! ')
    elif jogador==1:
        print('DEU EMPATE! ')
    elif jogador==2:
        print('O VOCÊ VENCEU! ')
    else:
        print('JOGADA INVALIDA! ')
elif computador==2:
    if jogador==0:
        print('O VOCÊ VENCEU! ')
    elif jogador==1:
        print('O COMPUTADOR VENCEU! ')
    elif jogador==2:
        print('DEU EMPATE! ')
    else:
        print('JOGADA INVALIDA! ')