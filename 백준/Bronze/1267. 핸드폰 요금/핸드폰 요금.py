n = input()
n = int(n)
y = 0  # 영식
m = 0  # 민식

c = map(int, input().split())

for i in c:
    y += (
        i // 30 + 1
    ) * 10  # 리스트에서 가져온 수를 30으로 나눈 몫 ex) 40/30하면 몫은 1 계산에 30이상 60미만이면 20이니 1을 추가 더해서 2를 맞춰서 요금을 곱
    m += (i // 60 + 1) * 15  # 위와 동일

if y == m:
    print("Y M", y)  # 가격이 같으면 영식부터 출력
elif y > m:
    print("M", m)  # 영식이 비싸면 민식부터 출력
else:
    print("Y", y)  # 민식이 비싸면 영식부터 출력