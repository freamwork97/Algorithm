s = input()
t = 0

for i in s:
    if i == "A" or i == "B" or i == "C":
        t += 3
    elif i == "D" or i == "E" or i == "F":
        t += 4
    elif i == "G" or i == "H" or i == "I":
        t += 5
    elif i == "J" or i == "K" or i == "L":
        t += 6
    elif i == "M" or i == "N" or i == "O":
        t += 7
    elif i == "P" or i == "Q" or i == "R" or i == "S":
        t += 8
    elif i == "T" or i == "U" or i == "V":
        t += 9
    elif i == "X" or i == "Y" or i == "Z" or i == "W":
        t += 10
    else:
        t += 11
print(t)
