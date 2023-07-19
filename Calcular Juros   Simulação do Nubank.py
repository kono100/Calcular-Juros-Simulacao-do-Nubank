
"""
Fórmula de juros composto
M=C(1+i)^t
Legenda
M = montante
C = capital
i = taxa de juros
t = tempo
"""


C = float(input("\nInforme capital para investimento: "))
i = 13.75/1000  # Taxa de juros do nubank
t = float(input("\nTempo de aplicação em meses: "))
M=C*(1 + i)**t
print ('\nJuros de retorno : ', M-C)
res = "{:.2f}".format(M)
print ('\nSeu rendimento total será: {} \n' .format(res)) 


from num2words import num2words

res = res.replace(',', '.') 
res = float(res)

inteiro, decimal = str(res).split('.')
num_ptbr = num2words(inteiro, lang='pt_BR')

if decimal and int(decimal) > 0: 
    decimal = decimal.ljust(2, '0')
    num_ptbr += ' vírgula ' + num2words(decimal, lang='pt_BR') + ' centavos'

print(f'\nNúmero por extenso: {num_ptbr.capitalize()}')
print()