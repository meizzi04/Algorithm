import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))

operator_cnt = list(map(int, input().split()))
operator = []

if operator_cnt[0] > 0:
    for i in range(operator_cnt[0]):
        operator.append('+')

if operator_cnt[1] > 0:
    for i in range(operator_cnt[1]):
        operator.append('-')


if operator_cnt[2] > 0:
    for i in range(operator_cnt[2]):
        operator.append('*')


if operator_cnt[3] > 0:
    for i in range(operator_cnt[3]):
        operator.append('/')

oper_per = list(permutations(operator, N-1))

maximum = -1e9  # -10억 = -1000000000
minimum = 1e9  # 10억 = 1000000000


def calculate():
    global maximum, minimum

    for i in oper_per:
        result = num[0]

        for j in range(1, N):
            if i[j-1] == '+':
                result += num[j]
            elif i[j-1] == '-':
                result -= num[j]
            elif i[j-1] == '*':
                result *= num[j]
            elif i[j-1] == '/':
                result = int(result / num[j])

        if result > maximum:
            maximum = result
        if result < minimum:
            minimum = result

calculate()

print(maximum)
print(minimum)