N, B = map(int, input().split())

convert_str = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

result = ''

while N > 0:
    N, mod = divmod(N, B)
    result += convert_str[mod]

print(result[::-1])