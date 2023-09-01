notas = []
nomes = []

# COMO DEFINIR O NÚMERO DE LINHAS E COLUNAS DE UMA MATRIZ
num = int(input("Quantas pessoas deseja informar nota? "))
num2 = int(input("Quantas notas por aluno deseja informar? "))
for i in range(num):
	notas.append([0] * num2)

x = 0
i = 0
y = 0
a = 0
z = 0
# COMO ARMAZENAR VALORES PERCORRENDO AS LINHAS:
for i in range(num):
    y = y + 1
    nome = input(f"\nInforme o nome do {y}° aluno: ")
    nomes.append(nome)
    for x in range(num2):
        z = z + 1
        notas[i][x] = int(input(f"Informe a {z}° nota: "))

# IMPRIMINDO OS ITENS DE UMA MATRIZ:
for i in range(num):
    a = a + 1
    print(f'\nNotas de {nomes[i]}: ', end = '')
    for x in range(num2):
        print(f'{notas[i][x]} ', end = '') 
        
