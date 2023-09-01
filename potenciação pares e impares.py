lista = list()

def potenciacao_em_lista():
    for itens in lista:
            if itens == lista[0] or lista[-1]:
                continue
            elif itens % 2 == 0:
                print(itens **2)
            elif itens % 2 != 0:
                print(itens **3)
    
