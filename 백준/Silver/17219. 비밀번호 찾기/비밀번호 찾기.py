N, M = map(int, input().split())

save = {}

for i in range(N):
    site, pw = input().split()
    save[site] = pw

for i in range(M):
    find_site = input()
    print(save[find_site])