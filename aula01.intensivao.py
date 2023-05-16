#Montar um relatório de controle de custos de todas as compras de mercadoria da empresa.
#Enviar um email com o total gasto, a quantidade de produtos comprados e o preço médio dos produtos.
#Entrar no google e acessar o link do Drive
#Baixar a planilha e calcular os valores propostos
#Calcular o total gasto com mercadorias
#Calcular a quantidade de produtos comprados
#Calcular o preço médio dos produtos

#Entrar no google e acessar o link do Drive
import pyautogui
from time import sleep
pyautogui.hotkey('win')
pyautogui.write('Chrome')
sleep(1)
pyautogui.press('Enter')
sleep(3)
pyautogui.click(x=314, y=47)
pyautogui.write('https://drive.google.com/drive/folders/160LsOE-hqu7W6i-E8v63N-ZsbWDbz7yV')
sleep(1)
pyautogui.press('Enter')
sleep(5)

#Baixar a planilha
pyautogui.click(x=560, y=372)
sleep(3)
pyautogui.click(x=452, y=192)

#Importar a base de dados e a planilha
import pandas as pd
import pyperclip

planilha = pd.read_csv(r"C:\Users\kaike\Downloads\Compras.csv", sep=';')

#Calcular o total gasto com as mercadorias
total = planilha['ValorFinal'].sum()

#Calular a quantidade de mercadorias
quantidade = planilha['Quantidade'].sum()

#Calcular o preço médio de uma mercadoria
preco_medio = total / quantidade

print(f'Os seus valores são {total:.2f}, {quantidade:.2f} e {preco_medio:.2f}')

#Abrir o email e enviar os resultados para o patrão
pyautogui.press('win')
pyautogui.write('Chrome')
sleep(1)
pyautogui.press('Enter')
sleep(5)
pyautogui.click(x=142, y=94)
sleep(6)
pyautogui.click(x=138, y=202)
sleep(6)
pyautogui.click(x=370, y=322, clicks = 2)
sleep(1)
pyautogui.write('kaike.carvalho@outlook.com')
sleep(2)
pyautogui.press('Enter')
sleep(2)
pyautogui.press('Tab')
sleep(1)
pyperclip.copy('Relatório da empresa')
pyautogui.hotkey('Ctrl', 'V')
sleep(1)
pyautogui.press('Tab')
sleep(1)
texto = (f'Aqui estão os relatórios da empresa\n'
        f'No período demonstrado na planilha a empresa atingiu:\n'
        f'O total gasto de R${total:,.2f} com mercadorias;\n'
        f'O total de {quantidade:,} mercadorias;\n'
        f'E o preço médio de R${preco_medio:,.2f} por mercadoria\n.'
        f'Atenciosamente, Kaike de Morais')
pyperclip.copy(texto)
pyautogui.hotkey('Ctrl', 'V')
sleep(5)
pyautogui.hotkey('Ctrl', 'Enter')