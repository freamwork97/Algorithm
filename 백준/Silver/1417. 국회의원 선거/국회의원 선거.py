n = int(input())  # 후보의 수

p = []  # 후보자표 목록 수
cnt = 0  # 매수할 표

for _ in range(n):  # 후보자 표 저장
    p.append(int(input()))

d = p[0]  # 다솜의 표
nd = p[1:]  # 다솜 제외한 나머지 표
if n == 1:  # 단일 후보시
    print(cnt)
else:
    nd.sort(reverse=True)  # 제일 많은 표부터 순차적으로
    # 제일 많은 후보자 표를 줄이고 다솜 표를 늘린다
    while nd[0] >= d:
        d += 1  # 다솜 표+1
        nd[0] -= 1  # 제일 많은 후보 표 -1
        cnt += 1  # 매수 표+1
        nd.sort(reverse=True)  # 한번더 정렬
    print(cnt)  # 매수한 표 출력