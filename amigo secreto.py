n = int(input())
lista = []
lista2 = []
lista3 = []
i = 0
a = 0
while i < n:
    presente = input().split(" ")
    lista.append(presente)
    i += 1
print("\n")

while True:
    try:
        opcao = input().split(' ')
        lista2.append(opcao)
        if lista2[a][0] == 'fim':
            break
        a += 1
    except EOFError:
        break

i = 0
a = 0
for a in range(len(lista2)):
    for i in range(len(lista)):
        if lista2[a][0] == lista[i][0]:
            if lista2[a][1] == lista[i][1]: 
                print("Uhul! Seu amigo secreto vai adorar")
            elif lista2[a][1] == lista[i][2]:
                print("Uhul! Seu amigo secreto vai adorar")
            elif lista2[a][1] == lista[i][3]:
                print("Uhul! Seu amigo secreto vai adorar")
            else:
                print("Tente Novamente!")
        else: 
            continue
        i += 1
    a += 1


