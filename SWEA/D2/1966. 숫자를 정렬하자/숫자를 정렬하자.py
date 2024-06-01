T = int(input())
for test_Case in range(1,T+1):
    c = int(input())
    num_list = list(map(int,input().split()))
    num_list.sort()
    print(f'#{test_Case}',*num_list)
