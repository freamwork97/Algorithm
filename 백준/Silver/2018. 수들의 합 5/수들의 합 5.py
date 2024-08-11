n = int(input())
count = 0
start, end, sum = 1, 1, 0

while start <= (n // 2) + 1:
    if sum < n:
        sum += end
        end += 1
    elif sum == n:
        count += 1
        sum -= start
        start += 1
    else:
        sum -= start
        start += 1

if n == 1 or n == 2:
    print(count)
else:
    print(count + 1)
