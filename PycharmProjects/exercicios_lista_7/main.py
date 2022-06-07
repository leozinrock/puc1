lista = []

for cont in range(5):
        lista.append(int(input("Digite um numero: ")))
local = int(input("Digite o numero para localizar"))
cont = 0
while cont < (len(lista)):
        if lista[cont] == local:
                break
        cont += 1
if cont <= (len(lista) - 1):
        print("valor encontrado na posição:", cont)
else:
        print("valor nao encontrado:")




