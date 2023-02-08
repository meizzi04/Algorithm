from itertools import permutations
num = []

N = int(input())

if 1 > N > 8 :
    print("입력 범위 초과")

for i in range(1, N+1) :
    num.append(i)

per = list(permutations(num, N))

for i in per :
    for j in i :
        print(j, end = " ")
    print()