num_list = list(map(int,input().split()))
num_list = sorted(num_list, reverse=True)

print(abs(num_list[0]-num_list[-1])+abs(num_list[1]-num_list[2]))
