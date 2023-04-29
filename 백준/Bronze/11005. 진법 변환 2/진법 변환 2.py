N, B = map(int, input().split())

arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = ''

while N != 0:
    ans += str(arr[N % B])
    N //= B

print(ans[::-1])