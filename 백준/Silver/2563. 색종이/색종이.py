SIZE = 100
black_area = [[0] * SIZE for _ in range(SIZE)]
num_squares = int(input())

for _ in range(num_squares):
    left, bottom = map(int, input().split())
    for i in range(left, left + 10):
        for j in range(bottom, bottom + 10):
            black_area[i][j] = 1

black_coverage = sum([sum(row) for row in black_area])
print(black_coverage)