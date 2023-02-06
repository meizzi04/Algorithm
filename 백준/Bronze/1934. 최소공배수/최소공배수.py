# 최소공배수(LCM) 계산 시 먼저 최대공약수(GCD) 구하기
## 유클리드 호제법(Euclidean algorithm) 사용
### LCM = A*B/GCD(A, B)

def GCD(A: int, B: int) : 
    if B == 0 :
        return A
    else :
        return GCD(B, A%B)

def LCM(A: int, B: int) :
    return (A*B)//GCD(A, B)

T = int(input())

for i in range(T) :
    A, B = list(map(int, input().split(" ")))
    print(LCM(A, B))
