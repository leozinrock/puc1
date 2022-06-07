import numpy as np

n_array = np.array ([[0,0,0],[0,0,0], [0,0,0]])
for linha in range (0,3):
    for coluna in range (0,3):
        n_array [linha] [coluna] = int(input(f'Digite um numero para a matriz {linha}, {coluna}: '))
        print('------------------------------')
        for linha in range (0,3):
            print(f'[{n_array [linha] [coluna]:^5}]', end = '')
        print()
    trace = np.trace(n_array)
    print("A resultado da matriz principal é de = ", trace)