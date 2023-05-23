from time import sleep
from math import sqrt, log

print("Bem-vindo(a) à Calculadora em Python! ")
sleep(1)
print("Insira dois valores e a operação que deseja calcular e veja a mágica acontecer!!")
sleep(1)

print("As operações disponíveis são:\n"
      "'+' para SOMA\n"
      "'-' para SUBTRAÇÃO\n"
      "'*' para MULTIPLICAÇÃO\n"
      "'/' para DIVISÃO\n"
      "'**' para POTÊNCIA\n"
      "'V' para RAIZ QUADRADA\n"
      "'lg' para LOGARÍTMO\n")
sleep(4)

n1 = float(input('Digite o primeiro valor a ser calculado: '))
n2 = float(input("Digite o segundo valor a ser calculado: "))
operador = input("Digite a operação que deseja calcular: ")
print("PROCESSANDO...")
sleep(3)

if operador == '+':
    print("operação selecionada: SOMA")
    print(f'{n1} + {n2} = {n1+n2}')
elif operador == '-':
    print('operação selecionada: SUBTRAÇÃO')
    print(f"{n1} - {n2} = {n1-n2}")
elif operador == '*':
    print('operação selecionada: MULTIPLICAÇÃO')
    print(f"{n1} * {n2} = {n1*n2}")
elif operador == '/':
    print('operação selecionada: DIVISÃO')
    print(f'{n1} / {n2} = {n1/n2}')
elif operador == '**':
    print('operação selecionada: POTÊNCIA')
    print(f'{n1} elevado a {n2} = {n1**n2}')
elif operador == 'V':
    print('operação selecionada: RAIZ QUADRADA')
    print(f'Raiz quadrada de {n1} = {sqrt(n1)}')
    print(f'Raiz qudrade de {n2} = {sqrt(n2)}')
elif operador == 'lg':
    print('Operação selecionada: LOGARÍTMO')
    print(f'Log de {n1} na base {n2} = {log(n1, n2)}')
    print(f'Log de {n2} na base {n1} = {log(n2, n1)}')
else:
    print('OPERAÇÃO INVÁLIDA')
    print('TENTE NOVAMENTE')