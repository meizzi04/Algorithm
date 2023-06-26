import sys

input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}

for i in range(N):
    eng = str(input().rstrip())

    if len(eng) >= M:
        if eng in dic:
            dic[eng] += 1
        else:
            dic[eng] = 1

dic = sorted(dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for i in dic:
    print(i[0])