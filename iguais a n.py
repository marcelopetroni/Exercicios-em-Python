lista = []
a = 0
b = 0
while a < 101:
    valores = input()
    lista.append(valores)
    a += 1

while b < 100:
    if lista[b] == lista[100]:
        print(b)
    b += 1
