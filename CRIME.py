perguntas = ['Telefonou para a vitíma?', 'Esteve no local do crime?', "Mora perto da vitima?", "Devia para a vitíma?", "Já trabalhou para a vitima?" ]
respostas = []
for pergunta in perguntas:
    resposta = int(input(pergunta+ "(1)Sim (0)Não"))
    respostas.append(resposta)
soma = 0
for resposta in respostas:
    soma = soma + resposta
if soma == 2:
    print("Inocente")
elif soma == 2:
    print("Suspeito")
elif soma <=4:
    print("Cumplice")
else:
    print("Assaltante")