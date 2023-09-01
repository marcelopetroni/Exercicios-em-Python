lista = []
while True:
    lista.clear()
    pedido = input("")
    if pedido == '0':
        print("Código inválido")
        break
    if pedido == '1':
        lista.append(2.50)
        print("Você escolheu Cachorro Quente")
    if pedido == '2':
        lista.append(4.75)
        print("Você escolheu X-Tudo")
    if pedido == '3':
        lista.append(3.25)
        print("Você escolheu Batata frita")
    if pedido == '4':
        lista.append(2.80)
        print("Você escolheu Refrigerante")
    if pedido == '5':
        lista.append(0.90)
        print("Você escolheu Pipoca")
    quantidade = int(input())
    valor = lista[0] * quantidade
    string = 'Sua conta é de R$'
    string2 = str(valor)
    string_final = string + string2
    print(string_final)
