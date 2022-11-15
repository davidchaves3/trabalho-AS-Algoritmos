i = 0
e = 1
lista = []
gabarito = []
# Cadastro do gabarito da Disciplina e o nome 
while i < 10:
  if i == 0:
    gabarito.append(input("Digite o Nome da Disciplina:"))
  gabarito.append(input(f"Digite a resposta da QUESTÃO {i} :"))
  i = i + 1
lista.append(gabarito)
i = 0
# Cadastro dos alunos e registro das respostas
while i < 2:
  e = 1
  alunos = []
  alunos.append(input("Digite o NOME do ALUNO :"))
  while e < 11:
    alunos.append(input(f"DIGITE A RESPOSTA DA QUESTÃO {e}"))
    e = e + 1
  lista.append(alunos)
  i = i + 1
i = 0
print(lista)

while i < len(lista):
  print(f"{lista[i]}")
  i = i + 1

i = 0
while i < len(lista):
  if lista[0][i] == lista[i][i]:
    
