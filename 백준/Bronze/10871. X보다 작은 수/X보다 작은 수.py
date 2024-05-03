n, x = map(int, input().split())
l = list(map(int, input().split()))

l = [i for i in l if i < x]
print(*l)