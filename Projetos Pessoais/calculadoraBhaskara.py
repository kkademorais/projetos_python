from math import sqrt
from time import sleep
print('Calcule agora a Equação do Segundo Grau de maneira automática!!')
print('-=-' * 30)
a = int(input('Me diga o número da variável "a": '))
b = int(input('Me diga o número da variável "b": '))
c = int(input('Me diga o número da variável "c": '))
print('Agora com as três variáveis vamos à equação!!')
print('PROCESSANDO...')
sleep(3)
print('-=-' * 30)
print(f'Sua equação é: {a}x2 + {b}x + {c} = 0')
print('Com a equação em mãos, vamos ao cálculo do delta!')
print('PROCESSANDO...')
sleep(3)
print('-=-' * 30)
delta = b*b - 4*a*c
print(f'O delta da sua equação é {delta}')
print('E agora vamos à resolução das raízes!')
print('PROCESSANDO...')
sleep(3)
print('-=-' * 30)
if delta < 0:
    print('Seu delta deu negativo, sendo assim, não existem raízes reais')
elif delta == 0:
    x = (-b + sqrt(delta)) / (2 * a)
    print(f'Seu delta é igual a 0, sendo assim, possui uma única raíz no valor de {x}')
else:
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)
    print(f'Seu delta deu positivo, sendo assim, possui duas raízes nos valores de {x1} e {x2}')
