N = int(input())
lista = []
num_negativos = []
i = 0
valor = list(input().split(" "))
lista.append(valor)
del valor[N:]

menor_num = min(valor)
print("Menor valor:", menor_num)
print("Posicao:", valor.index(menor_num))
print(valor[0])

 
