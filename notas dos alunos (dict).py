dados = dict()
todos_dados = list()
i = 0
while True:
    dados.clear()
    while True:
        dados['nome'] = str(input("Qual é seu nome? \n"))
        dados['matricula'] = input("Qual é seu número de matricula?\n")
        dados['materia'] = input("Diga todas as matérias que você estuda abaixo:\n").split(" ")
        dados['notas'] = input("Diga todas as respectivas notas das matérias informadas acima\n").split(" ")
        todos_dados.append(dados.copy())
    
        resp = input("Quer continuar? 'sim' para continuar e 'não' para parar\n")
        if resp == 'não' or resp == 'Não' or resp == 'N' or resp == 'n':
            break
    if resp == 'não' or resp == 'Não' or resp == 'N' or resp == 'n':
        break     

while True:
    aluno = input("Quem você deseja achar no sistema?\n")
    for i in range(len(todos_dados)):
        item = todos_dados[i]
        if aluno == item['nome']:
            print(todos_dados[i])
        i += 1
    opcao = str(input("Quer continuar? ('s' para sim e 'n' para não)\n"))
    if opcao == "n" or opcao == "N":
            break
    
