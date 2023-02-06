N = int(input())
nums = list(map(int, input().split(" ")))
primeNum = 0 # 소수의 개수

def prime(A : int) :
    if A < 2 : # 2 미만은 소수, 합성수 X
        return False

    for i in range(2, A) :    
        if A%i == 0 :
            return False
    return True

for i in range(N) :
    if prime(nums[i]) :
        primeNum += 1

print(primeNum)