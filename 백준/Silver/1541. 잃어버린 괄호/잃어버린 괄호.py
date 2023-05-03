a = input().split('-')
operand = []

for i in a:
    cnt = 0
    operator = i.split('+')
    for j in operator:
        cnt += int(j)
    operand.append(cnt)

n = operand[0]
for i in range(1, len(operand)):
    n -= operand[i]
print(n)