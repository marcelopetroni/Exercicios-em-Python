dicionario = {}
i = 0
# ARAMAZENANDO ITENS EM UM DICIONÁRIO VAZIO: 
# (se contivesse itens, seria ideal uma validação para ver se já não existe o novo item informado no dicionário)
for i in range(3):
    nome = input("Informe seu nome: ")
    idade = int(input("Informe sua idade: "))
    dicionario[nome] = idade
print(dicionario, "\n")

# MUDANDO ITENS DO DICIONÁRIO INFORMADO:
nome = input("Informe um nome para mudar sua idade: ")
if nome in dicionario.keys():
    idade = int(input("Informe uma nova idade: "))
    dicionario[nome] = idade
    print(dicionario)
else:
    while(nome not in dicionario.keys()):
        print("Nome não encontrado no dicionário. Reinforme um nome válido para mudar seus dados:")
        nome = input("Nome: ")

idade = int(input("Nova idade: "))
dicionario[nome] = idade
print(dicionario)
    
