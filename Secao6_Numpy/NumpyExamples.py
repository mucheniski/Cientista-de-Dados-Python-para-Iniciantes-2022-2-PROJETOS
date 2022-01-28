import numpy as np
import sys

# Lista comum
listaA = [1, 2, 3, 4, 5]

# Array numpy
listaB = np.array([1, 2, 3, 4, 5])

print(listaA)
print(listaB)

# Ver quanto em bytes cada um gasta
print(f'Tamanho listaA: {sys.getsizeof(listaA)}')
print(f'Tamanho listaB: {listaB.nbytes}')