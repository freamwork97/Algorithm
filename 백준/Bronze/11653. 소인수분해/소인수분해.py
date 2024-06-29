n = int(input())
answer = []

x = 2
while x <= n:
    if n % x == 0:
        answer.append(x)
        n //= x
    else:
        x += 1

for i in answer:
    print(i)