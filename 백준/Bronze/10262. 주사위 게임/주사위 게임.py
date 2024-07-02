g = list(map(int, input().split()))
s = list(map(int, input().split()))

if sum(g) > sum(s):
    print('Gunnar')
elif sum(g) < sum(s):
    print('Emma')
else:
    print('Tie')