import sys

input = sys.stdin.readline

N = int(input())
user = set()
cnt = 0

for i in range(N):
    txt = str(input().rstrip())

    if txt == "ENTER":
        user.clear()
    else:
        if txt not in user:
            user.add(txt)
            cnt += 1

print(cnt)