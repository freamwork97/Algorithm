n = int(input())
answer = 1
if n == 0:
    print(answer)
else:
    for i in range(n,0,-1):
        answer *=i
    print(answer)