# 조합(combinations 함수를 사용하여 순서 고려하지 않고 중복 없이 선택)
from itertools import combinations

def GCD(A : int, B : int) :
    if B == 0 :
        return A
    else :
        return GCD(B, A%B)

T = int(input())

for i in range(T) :
    arr = list(map(int, input().split()))
    sum = 0
    for j in list(combinations(arr[1:], 2)) :
        if j[0] > j[1] : # A로 B를 나눠야 하기 때문에 A가 더 커야 한다.
            sum += GCD(j[0], j[1])
        else :
            sum += GCD(j[1], j[0])

    print(sum)
