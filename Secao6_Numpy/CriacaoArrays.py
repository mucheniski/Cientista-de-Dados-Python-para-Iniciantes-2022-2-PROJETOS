import numpy as np

# Criação de array de 1D
array1D = np.array([1, 2, 3])
print(f'Array de uma dimensão {array1D} '
      f'- shape {array1D.shape} '
      f'- número de dimensões {array1D.ndim} '
      f'- tipo {array1D.dtype}')

print()
print('*'*500)
print()

# Criação de array de 2D
array2D = np.array([[1, 2, 3], [4, 5, 6]])
print(f'Array de duas dimensões {array2D} '
      f'- shape {array2D.shape} '
      f'- número de dimensões {array2D.ndim} '
      f'- tipo {array2D.dtype}')

print()
print('*'*500)
print()

# Criação de array de 3D
array3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(f'Array de trez dimensões {array3D} '
      f'- shape {array3D.shape} '
      f'- número de dimensões {array3D.ndim} '
      f'- tipo {array3D.dtype}')
