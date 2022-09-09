#Leia a largura e altura de uma parede em metros, calcule a área e a quantidade de tinta para pintar
# cada litro pinta 2m²
larg = float(input('Qual a largura da parede em metros? '))
alt = float(input('Qual a altura? '))
área = larg * alt
print('Sua parede tem {}x{} e sua área é de {}m²'.format(larg, alt, área))
tinta = área / 2
print('Você vai precisar de {}litros de tinta para pintar essa parede.'.format(tinta))
