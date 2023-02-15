N = int(input())
num = list(map(int, input().split()))

for i in range(N-1, 0, -1) :
    if num[i] < num[i-1] :
        for j in range(N-1, 0, -1) :
            if num[j] < num[i-1] :
                num[j], num[i-1] = num[i-1], num[j]
                num = num[:i] + sorted(num[i:], reverse=True)

                for k in num :
                    print(k, end = " ")
                exit()
print(-1)