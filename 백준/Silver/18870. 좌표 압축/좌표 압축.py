N = int(input())
coor = list(map(int, input().split()))
coor_ = sorted(list(set(coor)))
cnt = {}

for i in range(len(coor_)):
    cnt[coor_[i]] = i

for i in coor:
    print(cnt[i], end=" ")