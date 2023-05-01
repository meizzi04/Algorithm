N = int(input())
arr = list(map(int, input().split()))
arr.sort()

sum = 0
result = 0

for i in arr:
    sum += i
    result += sum

print(result)