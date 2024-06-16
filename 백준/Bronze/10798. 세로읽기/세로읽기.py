matrix = [list(input()) for _ in range(5)]
answer = ''
for i in range(5):
    while len(matrix[i]) < 15:
        matrix[i].append('')

for j in range(15):
    for i in range(5):
        if matrix[i][j] != '':
            answer += matrix[i][j]
print(answer)