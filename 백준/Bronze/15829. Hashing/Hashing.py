# 50점
L = int(input())
arr = input()
result = 0

for i in range(L):
    result += (ord(arr[i])-96) * (31**i)

print(result)

# 100점
L = int(input())
arr = input()
M = 1234567891
result = 0

for i in range(L):
    result += (ord(arr[i])-96) * (31**i)

print(result % M)
