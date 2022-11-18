# Trabalho de Algoritmos
# GRUPO - Maevy Dias; Arthur Almeida; David Chaves


i = 1 # O contador foi inicializado em 1 para acompanha o número das questão que vai ser mostrado na tela
e = 1 # O contador foi inicializado em 1 para acompanha o número das questão que vai ser mostrado na tela
cont = 0

lista = [] #Lista principal que vai armazenar o gabarito da prova e o nome da Disciplina e o nome dos Alunos e sus respostas
gabarito = [] # lista que vai aguardar o nome da disciplina e o gabarito da prova
classificados = [] #Lista para os alunos que tiram nota maior ou igual a 5
desclassificados = [] #Lista para os alunos que tiram nota menor ou que 5

# Cadastro do gabarito da Disciplina e o nome 
while i < 11:
  if i == 1: #Condicinal para quando o contador for igual a 1 mostre a mensagem para adicional a disciplina
    gabarito.append(input("Digite o Nome da Disciplina: "))
  gabarito.append(input(f"Digite a resposta da QUESTÃO {i} ==> "))
  i = i + 1
lista.append(gabarito)

i = 0
# Cadastro dos alunos e registro das respostas
while i < 30:
  e = 1 # Declarei o contador dentro do lado para que toda vez que repetir o contador volte ao valor inicial
  alunos = []
  alunos.append(input("Digite o NOME do ALUNO : "))
  #Laço de repetição para registrar a respostas da Prova 
  while e < 11: 
    alunos.append(input(f"DIGITE A RESPOSTA DA QUESTÃO {e} ==> "))
    e = e + 1
  # Zerando o contador e a variável nota para que toda vez que iniciar o laço retorne ao valor 0
  nota = 0
  cont = 0
  # Verificação dos acertos de cada Aluno na prova
  while cont < len(alunos):
    if alunos[cont] in gabarito[cont]:
      nota = nota + 1
    cont = cont + 1
  # Verifando se o aluno foi classificado ou desclassificado
  if nota >= 5:
    classificados.append(alunos[0])
    # Se ele tiver a nota maior ou igual a 5 seu nome vai ser ADD na lista Classificados
  elif nota < 5:
    # Caso ele tire uma NOTA menor que 5 o nome vai ser ADD na lista Desclassificados
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

    
