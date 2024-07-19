n = ''
while True:

    try:
        s = input()

        n += s
    except EOFError:
        break
l = n.split(',')
answer = 0
for i in l:
    answer += int(i)
print(answer)