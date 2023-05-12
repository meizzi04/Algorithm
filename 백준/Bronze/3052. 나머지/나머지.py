num = []
remainder = []

for i in range(10):
    num.append(int(input()))

    remainder.append(num[i] % 42)

print(len(set(remainder)))