while i < n:
    if lista[i][0] == lista2[i][0]:
        if lista[i][1] == lista2[i][1] or lista[i][1] == lista2[i][2] or lista2[i][1] == lista[i][3]:
            print("Uhul! Seu amigo secreto vai adorar")
        elif lista[i][2] == lista2[i][1] or lista[i][2] == lista2[i][2] or lista2[i][2] == lista[i][3]:
            print("Uhul! Seu amigo secreto vai adorar")
        elif lista[i][3] == lista2[i][1] or lista[i][3] == lista2[i][2] or lista2[i][3] == lista[i][3]:
            print("Uhul! Seu amigo secreto vai adorar")
        else:
            print("Tente Novamente!")
    i += 1

possibilidades = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '!', '?', '@', '#', '$', '%', '.', ';', ',', '/', ':']
    



