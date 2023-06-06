a, b, c = map(int, input().split())
long = max(a, b, c)
short = sum((a, b, c)) - long

while long >= short:
    long -= 1
print(long + short)