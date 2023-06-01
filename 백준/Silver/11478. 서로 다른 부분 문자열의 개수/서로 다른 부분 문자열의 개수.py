S = str(input())
result = set()

for i in range(len(S)):
    for j in range(i, len(S)):
        tmp = S[i : j + 1]
        result.add(tmp)
        
print(len(result))