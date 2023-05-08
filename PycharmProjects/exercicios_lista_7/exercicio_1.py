vetor = []

for cont in range(10):
    valor = int(input("Digite um numero: "))
    vetor.append(valor)

print(vetor)

argPesquisa = int(input("Digite o numero para busca: "))

if vetor.count(argPesquisa) == 0:
    print("Nao está no vetor")
else:
    print("Dado encontrado na posição: ",
vetor.index(argPesquisa))


print("caceta")