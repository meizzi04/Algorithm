N = int(input())
num = []

for i in str(N):
    num.append(i)

num.sort(reverse=True)

for i in num:
    print(i, end='')