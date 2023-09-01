frase = str(input())
dicionario = dict()

for i in frase:
    contador = frase.count(i)
    dicionario[i] = contador 
    dicionario_contrario = sorted(dict.items(dicionario), reverse=True)
    
for i in dicionario_contrario:
    print(i[0],i[1])