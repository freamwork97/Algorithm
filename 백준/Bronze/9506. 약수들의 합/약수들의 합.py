while True:
    n = int(input())
    if n == -1:
        break
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    divisors = divisors[:-1]
    if sum(divisors) != n:
        print(f'{n} is NOT perfect.')
        continue
    for i in range(len(divisors)):
        if i == 0:
            print(f'{n} = {divisors[i]}', end=' ')
        else:
            print(f'+ {divisors[i]}', end=' ')