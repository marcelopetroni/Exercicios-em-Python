texto = input("Escreva um texto:\n").split(" ")

while True:
    opcao = str(input('''Escolha ['c'] para adicionar uma frase nova ao texto\n        ['r'] para mostrar o texto escrito até o momento 
        ['u'] para modificar alguma parte do texto\n        ['d'] para deletar alguma parte do texto\n        
        ['s'] para salvar como arquivo em formato txt\n        ['o'] para abrir o arquivo\n        ['e'] para sair da aplicação\n'''))

    if opcao == 'c':
        texto.append(input("O que deseja adicionar ao texto?\n"))
        print(*texto, sep = ' ')
    if opcao == 'r':
        print(*texto, sep = ' ')
    if opcao == 'u':
        index = int(input("Informe o indice da palavra que deseja mudar:\n"))
        antes = str(input('Escreva a parte do texto que deseja substituir:\n'))
        depois = str(input('Escreva o que deseja por no lugar:\n'))
        
        texto[index] = depois
        print(*texto, sep = ' ')
    if opcao == 'd':
        item_removido = input("Escolha o que deseja remover:\n")
        for item in texto:
            if item == item_removido:
                texto.remove(item)
        print(*texto, sep = ' ')
    
    if opcao == 's':
        escolha_do_usuario = input("escolha um nome para seu arquivo\n")

    if opcao == 'o':
       with open(texto, 'r') as arquivo:
           for linha in arquivo:
                print(linha)
    if opcao == 'e':
        arquivo.close()
    
    resp = input("Você deseja continuar? 'sim' para continuar, 'não' para parar\n")
    if resp == "não" or resp == "Não" or resp == "N" or resp == "n":
        break

with open(escolha_do_usuario.txt, 'r') as arquivo:
    for valor in escolha_do_usuario:
        arquivo.write(str(valor) + '\n')

