z = 0
multiplicador = int(input())
resp = 0
#Insira o código aqui

while z in range(0,11):
    num = z
    resp = num * multiplicador
    z += 1
    print('{} x {} = {}'.format(num, multiplicador, resp))

 