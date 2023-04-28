T = int(input())
arr = []
for i in range(T):
    arr.append(str(input()))

result = []
for i in arr:
    cnt = 0
    for j in i:
        if j == 'O':
            cnt += 1
            result.append(cnt)
        else:
            cnt = 0
            result.append(cnt)
    print(sum(result))
    result.clear()