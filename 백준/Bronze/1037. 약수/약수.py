N_num = int(input())
N_real = list(map(int, input().split()))

N_max = max(N_real)
N_min = min(N_real)

print(N_max * N_min)