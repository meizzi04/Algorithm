import sys
input = sys.stdin.readline

N = int(input())
num = []

for i in range(N):
    num.append(int(input()))

num.sort()

mean = round(sum(num) / N)  # 산술평균
median = num[len(num)//2]  # 중앙값

# 최빈값
m = dict()
for i in num:
    if i in m:
        m[i] += 1
    else:
        m[i] = 1

mx = max(m.values())
mx_mode = []

for i in m:
    if mx == m[i]:
        mx_mode.append(i)

if len(mx_mode) > 1:
    mode = mx_mode[1]
else:
    mode = mx_mode[0]

# 범위
range = max(num)-min(num)

print(mean)
print(median)
print(mode)
print(range)