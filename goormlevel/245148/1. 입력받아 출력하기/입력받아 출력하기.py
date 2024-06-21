n = int(input())
char1, char2 = input().split()

for i in range(n):
    for j in range(n):
        if j % 2 == 0:
            if (i + j) % 2 == 0:
                print(char1, end=" ")
            else:
                print(char2, end=" ")
        else:
            print(char2, end=' ')
    print()
