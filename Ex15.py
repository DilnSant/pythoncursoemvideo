#Programa que solicita km e dias de um carro alugado, calculando o valor:
#diária: R$60,00 e km: R$ 0,15

dias = int(input('Quantos dias usou o veículo? '))
km = float(input('Qual a kilometragem realizada? '))
valor = (dias * 60.00) + (km * 0.15)
print('Com a diária de {} dias e tendo rodado {} km o valor total foi de R$ {:.2f}'.format(dias, km, valor))
