chess = [['w', 'b', 'w', 'b', 'w', 'b', 'w', 'b'],
         ['b', 'w', 'b', 'w', 'b', 'w', 'b', 'w'],
         ['w', 'b', 'w', 'b', 'w', 'b', 'w', 'b'],
         ['b', 'w', 'b', 'w', 'b', 'w', 'b', 'w'],
         ['w', 'b', 'w', 'b', 'w', 'b', 'w', 'b'],
         ['b', 'w', 'b', 'w', 'b', 'w', 'b', 'w'],
         ['w', 'b', 'w', 'b', 'w', 'b', 'w', 'b'],
         ['b', 'w', 'b', 'w', 'b', 'w', 'b', 'w']]
chk = 0

unit = [list(input()) for _ in range(8)]

for i in range(8):
    for j in range(8):
        if unit[i][j] == 'F' and chess[i][j] == 'w':
            chk += 1
print(chk)