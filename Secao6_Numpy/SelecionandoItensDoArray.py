import numpy as np

# Criando um array 2D (2, 4)
listaA = np.array([
    [2, 3, 4, 5],
    [6, 7, 8, 9]
])

print(listaA.shape)

# Buscando um valor pela posição, buscando o 8
# array[row, column]
print(listaA[1, 2])

# Contagem regressiva pode ser feita também
# Buscando o 8 regressivo
print(listaA[1, -2])

# Buscando apenas uma row zero, vírgula todas as colunas
print(listaA[0,:])

# Buscar valor específico em arrays diferentes, todas as rows da coluna um
print(listaA[:,1])