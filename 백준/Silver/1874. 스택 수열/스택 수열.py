n = int(input())
stack = []
result = []
flag = 0
tmp = 1

for i in range(n):
    num = int(input())

    while tmp <= num:
        stack.append(tmp)
        result.append('+')
        tmp += 1

    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        flag = 1
        break

if flag == 0:
    for i in result:
        print(i)