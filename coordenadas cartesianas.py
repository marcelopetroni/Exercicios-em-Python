import math

x = float(input())
y = float(input())
tupla = (x,y)
x2 = float(input())
y2 = float(input())
tupla2 = (x2,y2)

distancia = (x2 - x)**2 + (y2 - y) ** 2
raiz = math.pow(distancia, 1/2)
print(raiz)