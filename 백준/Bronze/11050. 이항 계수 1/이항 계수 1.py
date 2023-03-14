N, K = map(int, input().split())
numerator = 1  # 분자
denominator = 1  # 분모

for i in range(K):
    numerator *= N-i
    denominator *= K-i

result = numerator//denominator

print(result)