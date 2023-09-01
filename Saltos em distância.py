lista = []
lista2 = []
i = 0
z = 1
x = 0
while True:
    nome = str(input())
    if nome == 'SAIR' or nome == 'sair':
        break
    salto = int(input())
    lista.append(salto)
    salto2 = int(input())
    lista.append(salto2)
    salto3 = int(input())
    lista.append(salto3)
    salto4 = int(input())
    lista.append(salto4)
    salto5 = int(input())
    lista.append(salto5)

while i < len(lista):
    if lista[i] < lista[i+1] and lista[i] < lista[i+2] and lista[i] < lista[i + 3] and lista[i] < lista[i + 4]:
        # menor = lista[i]
        media = (lista[i+1] + lista[i+2] + lista[i+3] + lista[i+4])/4
        lista2.append(media)
    elif lista[i+1] < lista[i] and lista[i+1] < lista[i+2] and lista[i+1] < lista[i + 3] and lista[i+1] < lista[i + 4]:
        # menor = lista[i+1]
        media = (lista[i] + lista[i+2] + lista[i+3] + lista[i+4])/4
        lista2.append(media)
    elif lista[i+1] < lista[i] and lista[i+2] < lista[i+1] and lista[i+2] < lista[i + 3] and lista[i+2] < lista[i + 4]:
        # menor = lista[i+2]
        media = (lista[i] + lista[i+1] + lista[i+3] + lista[i+4])/4
        lista2.append(media)
    elif lista[i+2] < lista[i] and lista[i+3] < lista[i+1] and lista[i+ 3] < lista[i + 2] and lista[i+3] < lista[i + 4]:
        # menor = lista[i+3]
        media = (lista[i] + lista[i+1] + lista[i+2] + lista[i+4])/4
        lista2.append(media)
    elif lista[i+4] < lista[i] and lista[i+4] < lista[i+1] and lista[i+4] < lista[i + 2] and lista[i+4] < lista[i +3]:
        # menor = lista[i+4]
        media = (lista[i] + lista[i+1] + lista[i+2] + lista[i+3])/4
        lista2.append(media)
    elif lista[i] == lista[i+1] and lista[i] == lista[i+2] and lista[i] == lista[i+3] and lista[i] == lista[i+4]:
        # não tem menor
        media = (lista[i] + lista[i+1] + lista[i+2] + lista[i+3]+ lista[i+4])/5
        lista2.append(media)

    i += 5
lista.sort(reverse = True)
lista2.sort(reverse = True)
print("\nO ranking foi definido como:")
print(lista2)
for itens in lista2:
    str(itens).split()
    print("O ", z,"°"," lugar teve uma média de ", itens, "e seu melhor salto foi de ", max(lista[x:x+5]) ," metros de altura")
    z += 1
    x += 5