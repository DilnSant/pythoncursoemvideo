#ORDEM DE PRECEDÊNCIA

print(5+3*2)
print(3*5+4**2)
print(3*(5+4)**2)

#OPERADORES ARITMÉTICOS
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro únumero: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é: {} \nO produto é: {} \nA divisão é: {:.3f}'.format(s, m, d))
print('Divisão inteira: {}'.format(di),end='  ###   ')
print('Potência: {}'.format(e))
