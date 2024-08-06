import sys

n = int(sys.stdin.readline())

stack = []
for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == '1':
        stack.append(int(command[1]))
    elif command[0] == '2':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == '3':
        print(len(stack))
    elif command[0] == '4':
        print(1 if not stack else 0)
    elif command[0] == '5':
        print(stack[-1] if stack else -1)
    else:
        pass