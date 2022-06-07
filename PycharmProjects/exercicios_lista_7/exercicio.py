alturas = []  
for cont in range(5):
    altura = int(input("Digite uma altura:"))
    alturas.append(altura)

soma = 0
for cont in range(len(alturas)):
    soma = soma + alturas[cont]

media = soma/5
print(media)

for cont in range(5):
