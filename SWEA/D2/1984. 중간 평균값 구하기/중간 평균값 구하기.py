T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    num_list = list(map(int,input().split()))
    num = round((sum(num_list)-max(num_list) -min(num_list))/8)
    print(f'#{test_case} {num}')
    # ///////////////////////////////////////////////////////////////////////////////////
