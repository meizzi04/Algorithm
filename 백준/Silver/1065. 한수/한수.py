N = int(input())

a = 0

for i in range(1, N + 1):
    li = list(map(int, str(i)))

    if i < 100:
        a += 1
    elif li[0] - li[1] == li[1] - li[2]:
        a += 1
print(a)