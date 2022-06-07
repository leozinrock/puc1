#funcao log
import matplotlib.pyplot as plt
import numpy as np
import math

def funcaoLog (x,base):
  return (math.log(x,base))

vetorX = np.arange(0.1,70,0.1)
print(vetorX)

#base log
base = 2
logaritmando = 8

#valor de y p/ cada valor de x
vetorY=[]
for log in vetorX:
  vetorY.append(funcaoLog(log,base))
print(vetorY)

fig = plt.figure(figsize=(5,5))

plt.plot(vetorX, vetorY, label='f(x) = log2(x)', color='c')

plt.title (f'f(x) = log{base}({logaritmando})')
plt.xlabel('eixo x')
plt.ylabel('eixo y')
plt.legend()
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.show()
fig.savefig('flog.png')