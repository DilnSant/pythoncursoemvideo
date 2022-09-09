#Lendo salário do funcionário e mostrando novo swalário com 15% de aumento:
salario = float(input('Informe o salário atual do funcionário: R$'))
novo = salario + (salario * 15 / 100)
print('O salário de R$ {:.2f} com 15% de aumento será de R${:.2f}'.format(salario, novo))

