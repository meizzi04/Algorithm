import sys

input = sys.stdin.readline
max = 10000
arr = [True for i in range(max+1)]

for i in range(2, 101) :
   if arr[i] :
      for j in range(i+i, max+1, i) :
        arr[j] = False

T = int(input())

for i in range(T) :
    n = int(input())

    a = n // 2

    for j in range(a, 1, -1) :
       if arr[j] and arr[n-j] :
          print(j, n-j)
          break