N = int(input())
meeting = []
last = 0  # 회의 마지막 시간
cnt = 0  # 회의 개수

for i in range(N):
    start, end = map(int, input().split())
    meeting.append([start, end])

meeting = sorted(meeting, key=lambda a: a[0])
meeting = sorted(meeting, key=lambda a: a[1])

for i, j in meeting:
    if i >= last:
        cnt += 1
        last = j

print(cnt)