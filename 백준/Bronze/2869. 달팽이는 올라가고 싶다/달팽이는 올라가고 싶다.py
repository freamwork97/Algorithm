import math

a,b,v = map(int, input().split())
days = (v - b) / (a - b)
print(math.ceil(days))