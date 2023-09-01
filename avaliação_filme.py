variavel_controle = 1
contador = 0; soma = 0; soma2 = 0
regular = 0; bom = 0; otimo = 0
conta = 0; conta2 = 0; conta3 = 0
idade_regular = 0; idade_bom = 0; idade_otimo = 0

while variavel_controle != 0:
        idade = int(input("Quantos anos você tem? (escolha 0 para sair do loop)\n"))
        soma += idade
        contador += 1

        if idade == 0:
            print("Programa finalizado, volte sempre!")
            break
        
        if idade > 120:
            print("Idade irregular a um ser humano, por favor reescreva-a")
            continue

        print("Escolha uma avaliação para o filme:\n","[1] Regular\n", "[2] Bom\n", "[3] Ótimo\n")
        avaliacao = int(input())
        soma2 += avaliacao

        if avaliacao == 0:
            print("Programa finalizado, volte sempre!")
            break
        
        if avaliacao != 1 and avaliacao != 2 and avaliacao != 3:
            print("Nota estabelecida indisponível, por favor escolha 1 para regular, 2 para bom ou 3 para ótimo")
            continue

        # A partir daqui comecei a armazenar os dados por nota
        if avaliacao == 1:
            regular += 1
            conta += avaliacao
            idade_regular += idade

        if avaliacao == 2:
            bom += 1
            conta2 += avaliacao
            idade_bom += idade

        if avaliacao == 3:
            otimo += 1
            conta3 += avaliacao
            idade_otimo += idade
        
# A partir daqui estabeleci condicionais caso de todos os usuários não aparecer uma nota regular, boa ou ótima e evitar a divisão por 0

        if regular != 0:
            media_idades = idade_regular/regular
        else:
            media_idades = 0

        if bom != 0:
            media_idades2 = idade_bom/bom
        else:
            media_idades2 = 0
        
        if otimo != 0:
            media_idades3 = idade_otimo/otimo
        else:
            media_idades3 = 0

percentual = (regular * 100)/ (contador - 1)
percentual2 = (bom * 100)/ (contador - 1)
percentual3 = (otimo * 100)/(contador - 1)
media_final = (soma2)/ (contador - 1)
        
print("\nDe acordo com os dados fornecidos pelos usuários do filme, foi estabelecido:")

print("\nUma quantidade de ", contador - 1, " pessoas foram ver o filme")

print("\nUma quantidade de ", regular, " pessoas que avaliaram regular, ", bom, " pessoas que avaliaram bom ", 
otimo, " que avaliaram otimo\n")

print("A média de idades dos usúarios que avaliaram ótimo foi de: ", media_idades3, " anos, para bom foi de: ",
media_idades2," anos e para regular foi de: ", media_idades, " anos\n")

print("O percentual de notas foram:\n ","\n", percentual3, "% para notas ótimas\n", percentual2, "% para notas boas\n",
percentual, "% para notas regulares")

print("\nA média final de notas para o filme foi: ", media_final, " de acordo com as avaliações do público")