import random
size = 5

matrix = [[random.randint(1,10) for _ in range(size)] for _ in range(size)]
for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()

print('*' * 32)

for i in range(size):
    for j in range(size):
        if i == j:
            tmp = matrix[i][j]
            matrix[i][j] = matrix[i][size - 1 - j]
            matrix[i][size - 1 - j] = tmp

for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()