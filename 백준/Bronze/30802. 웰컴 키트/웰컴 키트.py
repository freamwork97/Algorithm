import math

n = int(input())

s = list(map(int, input().split()))
t, p = map(int, input().split())
t_bundle = sum([math.ceil(size / t) for size in s])
print(t_bundle)

p_bundle = n // p
p_single = n % p
print(p_bundle, p_single)