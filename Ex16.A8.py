#import math
#num = int(input('Digite um número: '))
#raiz = math.sqrt(num)
#print('A raiz de {} é igual a {:.2f}'.format(num, math.ceil(raiz)))
#A função (math.ceil) antes da raiz arredonda p/ cima#

#(importa somente raiz e arredond. p/ baixo)
from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))


