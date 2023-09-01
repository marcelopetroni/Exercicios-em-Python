lista = []
lista2 = []
lista3 = []
lista4 = []
i = 0
x = 0
soma_itens = 0
soma_itens2 = 0
while True:
    usuario = str(input("Qual é seu nome? (informe '0' para parar)\n"))
    lista4.append(usuario)
    if usuario == '0':
        break
    renda = float(input("Qual é sua renda?\n"))
    lista.append(renda)

while True:
    conta = str(input("Qual é o nome da conta? (informe '0' para parar)\n"))
    if conta == '0':
        break
    valor = float(input("Qual é o valor da conta a ser pagada?\n"))
    lista2.append(valor)

for item in lista:
    soma_itens += item

for item in lista2:
    soma_itens2 += item

if soma_itens < soma_itens2:
    print("Sua família precisa cortar gastos para pagar as contas")

conta = soma_itens2/soma_itens

while i < len(lista):
    calculo = conta * lista[i]
    lista3.append(calculo)
    i += 1

for item in lista4:
    try:
        print(item, "irá pagar ", lista3[x])
    except IndexError:
        break
    x += 1