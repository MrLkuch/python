# exo 6.18
# Avec le même tableau en 2 dimensions, affichez toutes les valeurs plus petites ou égales à 50 ainsi que leur cordoonnées (ligne et colonne)
# Vous pouvez réutiliser la variable `size` qui a permis de construire le tableau en 2 dimensions

import random

size = 5
matrix = []

for _ in range(0, size):
    row = [random.randint(40, 100) for _ in range(0, size)]
    matrix.append(row)

print(matrix)

# réponse 6.18

for i in range(size):
    for j in range(size):
        if matrix[i][j] <= 50:
            print(matrix[i][j], f"ligne: {i+1}", f"colonne: {j+1}")