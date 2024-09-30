n = int(input())
if n < 10:
    n *= 10
copy_n = n
chk = 0
while True:
    a = n // 10
    b = n % 10
    c = (a + b) % 10
    n = b * 10 + c
    chk += 1
    if n == copy_n:
        break
print(chk)