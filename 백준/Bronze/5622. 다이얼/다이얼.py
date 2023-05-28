dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
alp = str(input())
result = 0

for i in range(len(alp)):
    for j in dial:
        if alp[i] in j:
            result += dial.index(j) + 3
print(result)