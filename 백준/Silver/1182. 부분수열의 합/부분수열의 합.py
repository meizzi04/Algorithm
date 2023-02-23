from itertools import combinations

N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

for i in range(1, N+1) :
    arr_comb = combinations(arr, i)

    for j in arr_comb :
        if sum(j) == S :
            cnt += 1

print(cnt)