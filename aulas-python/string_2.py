nome = "Rebecca"
idade = 15
profissao = "Programador"
linguagem = "Python"
saldo = 45.423

dados = {"nome": "Rebecca", "idade": 15}

print("Nome: %s Idade: %d" % (nome, idade))
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {0} Idade: {1}".format(nome, idade))
print("Nome: {nome} Idade: {idade}".format(nome=nome,  idade=idade))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} idade: {idade}")
print(f"Nome: {nome} idade: {idade} saldo: {saldo:.2f}")
print(f"Nome: {nome} idade: {idade} saldo: {saldo:10.2f}")
