nota = float(input("Quanto você tirou na primeira prova?\n"))
if nota > 10 or nota < 0:
    print("Valor incoerente, escreva uma nota entre 0 - 10")
    quit()

nota2 = float(input("Quanto você tirou na segunda prova?\n"))
if nota > 10 or nota < 0:
    print("Valor incoerente, escreva uma nota entre 0 - 10")
    quit()

nota3 = float(input("Quanto você tirou na terceira prova?\n"))
if nota > 10 or nota < 0:
    print("Valor incoerente, escreva uma nota entre 0 - 10")
    quit()

media = (nota + nota2 + nota3)/3

if media >= 7:
    print("Parabéns, você passou por média!")
if media >= 5 and nota < 7:
    print("Sinto muito, você vai para a recuperação.")
if media < 5:
    print("Sinto muito, você reprovou!")

