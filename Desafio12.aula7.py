# Algoritimo que lê o preço do produto e mostra seu novo preço com 5% de desconto
preço = float(input('Preço do produto: R$'))
desc = preço - (preço * 5 / 100)
print('O produto de R$ {:.2f}, com desconto vai custar R$:{:.2f}'.format(preço, desc))