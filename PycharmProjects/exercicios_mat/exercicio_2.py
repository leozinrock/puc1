import matplotlib.pyplot as plt
import numpy as np


def funcaoExponencial(base,expoente):
   return(base**expoente)


vetorx = np.arange(-7, 7, 0.1)

print(vetorx)


base = 0.7
expoente = 10

vetorY = []
for expo in vetorx:
    vetorY.append(funcaoExponencial(base, expo))

print(vetorY)


fig = plt.figure(figsize=(5, 5))



plt.plot(vetorx, vetorY, label = 'Funcao Exponencial', color = 'g')

plt.title(f'f(x)={base}^{expoente}')
plt.xlabel('eixoX')
plt.ylabel('eixoy')
plt.legend()
plt.grid(True, which='both')
plt.axhline(y=0, color= 'k')
plt.axvline(x=0, color='k')
plt.show()
fig.savefig('FExp.png')