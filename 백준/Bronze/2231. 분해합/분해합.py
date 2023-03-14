N = int(input())

for i in range(1, N+1):
    i_sum = sum(map(int, str(i)))
    total = i_sum + i

    if total == N:
        print(i)
        break
    elif i == N:
        print(0)