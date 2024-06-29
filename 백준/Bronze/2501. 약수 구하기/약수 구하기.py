n1, n2 = map(int, input().split())
divisors = [i for i in range(1, n1 + 1) if n1 % i == 0]
print(divisors[n2 - 1] if n2 <= len(divisors) else 0)