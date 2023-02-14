N = int(input())
num = list(map(int, input().split()))

for i in range(N-1, 0, -1) : # 뒤에서부터 비교
    if num[i] > num[i-1] : # 뒤에 있는 값이 크면 내림차순이 아니라는 의미
        for j in range(N-1, 0, -1) : # 다시 뒤에서부터 비교
            if num[i-1] < num[j] :
                num[i-1], num[j] = num[j], num[i-1]
                num = num[:i] + sorted(num[i:])

                for k in num :
                    print(k, end = ' ')
                exit()
print(-1)