T = int(input())
count = 0

for _ in range(T):
    word = input()
    if list(word) == sorted(word, key=word.find):
        count += 1

print(count)