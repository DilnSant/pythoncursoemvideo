#Converter valor da carteira em quantos dólares pode comprar:
#Considere: US$1,00+R$3,27

real = float(input('Quantos reais há na carteira? R$'))
dolar = real / 3.27
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar), 'dólares')

