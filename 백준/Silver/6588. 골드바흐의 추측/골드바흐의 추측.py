# 소수 : True, 소수 x : False
import sys
max = 1000000
arr = [True for k in range(max+1)]

# 에라토스테네스의 체 사용
for i in range(2, 1001) :
   if arr[i] :
      for j in range(i+i, max+1, i) :
        arr[j] = False

while True :
    n = int(sys.stdin.readline())

    if n == 0 :
       break 

    for i in range(3, len(arr)) :
       if arr[i] and arr[n-i] :
         print(n, "=", i, "+", n-i)
         break