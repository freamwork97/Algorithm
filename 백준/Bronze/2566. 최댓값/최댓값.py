matrix = [list(map(int, input().split())) for _ in range(9)]
max_value = 0
max_position = (0, 0)

for i in range(9):
    for j in range(9):
        if matrix[i][j] >= max_value:
            max_value = matrix[i][j]
            max_position = (i + 1, j + 1)

print(max_value)
print(*max_position)