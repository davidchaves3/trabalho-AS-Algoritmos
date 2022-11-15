i = 1
e = 1
cont = 0
lista = []
gabarito = []
classificados = []
desclassificados = []
# Cadastro do gabarito da Disciplina e o nome 
while i < 11:
  if i == 1:
    gabarito.append(input("Digite o Nome da Disciplina: "))
  gabarito.append(input(f"Digite a resposta da QUESTÃO {i} ==> "))
  i = i + 1
lista.append(gabarito)
i = 0
# Cadastro dos alunos e registro das respostas
while i < 2:
  e = 1
  alunos = []
  alunos.append(input("Digite o NOME do ALUNO : "))
  while e < 11:
    alunos.append(input(f"DIGITE A RESPOSTA DA QUESTÃO {e} ==> "))
    e = e + 1
  # Zerando as variáveis toda vez que vai registrar um novo Aluno
  nota = 0
  cont = 0
  # Verificação dos acertos de cada Aluno na prova
  while cont < len(alunos):
    if alunos[cont] in gabarito:
      nota = nota + 1
    cont = cont + 1
  # Verifando se o aluno foi classificado ou desclassificado
  if nota > 4:
    classificados.append(alunos[0])
  elif nota < 5:
    desclassificados.append(alunos[0])
  # Adicionando o NOME e a resposta dos Alunos na LISTA PRINCIPAL
  lista.append(alunos)
  i = i + 1
# Imprimindo o gabarito da prova e a resposta de cada ALUNO
i = 0
while i < len(lista):
  print(f"{lista[i]}")
  i = i + 1
# Imprimindo o NOME dos Alunos que foram CLASSIFICADOS
i = 0
print("ALUNOS CLASSIFICADOS")
while i < len(classificados):
  print(classificados[i])
  i = i + 1
# Imprimindo o NOME dos Alunos que foram DESCLASSIFICADOS
i = 0
print("ALUNOS DESCLASSIFICADOS")
while i < len(desclassificados):
  print(desclassificados[i])
  i = i + 1

    
