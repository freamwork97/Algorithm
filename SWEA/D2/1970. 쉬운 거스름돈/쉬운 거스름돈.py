T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    n_list = [0]*8
    if N >= 50000:
        while N >=50000:
            N-=50000
            n_list[0]+=1
    if N >= 10000:
        while N >=10000:
            N-=10000
            n_list[1]+=1
    if N >= 5000:
        while N >=5000:
            N-=5000
            n_list[2]+=1
    if N >= 1000:
        while N >=1000:
            N-=1000
            n_list[3]+=1
    if N >= 500:
        while N >=500:
            N-=500
            n_list[4]+=1
    if N >= 100:
        while N >=100:
            N-=100
            n_list[5]+=1
    if N >= 50:
        while N >=50:
            N-=50
            n_list[6]+=1
    if N >= 10:
        while N >=10:
            N-=10
            n_list[7]+=1
    print(f'#{test_case}')
    print(*n_list)