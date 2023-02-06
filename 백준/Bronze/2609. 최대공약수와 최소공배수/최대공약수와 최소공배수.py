def GCD(A : int, B : int) :
    if B == 0 :
        return A
    else :
        return GCD(B, A%B)

def LCM(A : int, B : int) :
    return (A*B)//GCD(A, B)

T = list(map(int, input().split(" ")))

print(GCD(T[0], T[1]))
print(LCM(T[0], T[1]))