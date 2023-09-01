contador = 1 

while contador > 0:
    print("Escolha três valores entre 0 e 255 para determinar uma cor (digite um valor negativo para parar)\n")
    
    r = int(input())
    if r > 255:
        print("Valor inválido com o intervalo 0 - 255, por favor reescreva os números.\n")
        continue
    if r < 0:
        print("Fim do programa! até mais")
        break

    g = int(input())
    if g > 255:
        print("Valor inválido com o intervalo 0 - 255, por favor reescreva os números.\n")
        continue
    if g < 0:
        print("Fim do programa! até mais")
        break

    b = int(input())
    if b > 255:  
        print("Valor inválido com o intervalo 0 - 255, por favor reescreva os números.\n")
        continue
    if b < 0:
        print("Fim do programa! até mais")
        break

    # Aqui começa as condicionais para cada cor
    if r == 0 and r == g and r == b:
        print("A cor será o preto")
     
    elif r == 255 and r == g and r == b:
        print("A cor será o branco")

    elif r == g and r == b:
        print("A cor será o cinza")

    elif r > g and r > b:
        print("A cor será o vermelho")

    elif g > r and g > b:
        print("A cor será o verde")

    elif b > g and b > r:
        print("A cor será o azul")

    elif r == g and r > b:
        print("A cor será o amarelo")

    elif r == b and r > g:
        print("A cor será o magenta")

    elif g == b and g > r:
        print("A cor será o ciano")
