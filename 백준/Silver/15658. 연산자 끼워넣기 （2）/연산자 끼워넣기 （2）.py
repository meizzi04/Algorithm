N = int(input())
num = list(map(int, input().split()))
operator_cnt = list(map(int, input().split()))

operator_real = ['+', '-', '*', '/']
operator = []

maximum = -1e9
minimum = 1e9

for i in range(4) :
    if operator_cnt[i] > 0 :
        for j in range(operator_cnt[i]) :
            operator.append(operator_real[i])

def calculate(current, result) :
    global maximum, minimum

    if current == N :
        maximum = max(maximum, result)
        minimum = min(minimum, result)
        return
   
    for i in range(4) :
        if not operator_cnt[i] == 0 :
            if i == 0 : # +
                tmp = result + num[current]
            elif i == 1 : # -
                tmp = result - num[current]
            elif i == 2 : # *
                tmp = result * num[current]
            elif i == 3 : # /
                if result < 0 : # 음수
                    tmp = int(-result // num[current])
                    tmp = -tmp
                else :
                    tmp = int(result // num[current])
            
            operator_cnt[i] -= 1
            calculate(current+1, tmp)
            operator_cnt[i] += 1

calculate(1, num[0])

print(maximum)
print(minimum)