#Calculadora Simples
from tkinter import *
from tkinter import ttk

janela = Tk ()
janela.title('Calculadora')
janela.geometry("235x318")

frame_tela = Frame(janela, width=235, height=50)
frame_tela.grid(row=0, column=0)
janela.mainloop()


# numero1 = 0
# numero2 = 0
# resultado = 0
# operacao = ''

# numero1 = int(input('Digite o primeiro valor: '))
# operacao = input('Digite a operação: ')
# numero2 = int(input('Digite o segundo valor: '))

# if operacao == '+':
#     resultado = numero1 + numero2
# elif operacao == '-':
#     resultado = numero1 - numero2
# elif operacao == '/':
#     resultado = numero1 / numero2
# elif operacao == '*':
#     resultado = numero1 * numero2
# else:
#     resultado = 'Opreação Inválida'

# print(str(numero1) + ' ' + str(operacao) +  ' ' + str(numero2) + ' = ' + str(resultado))
       