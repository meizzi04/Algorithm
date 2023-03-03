N = int(input())

sugar_bag = 0

while N >= 0:
    if N % 5 == 0:  # 5의 배수인 경우
        sugar_bag += N // 5  # 5로 나눈 몫
        print(sugar_bag)
        break
    else:
        N -= 3
        sugar_bag += 1
else:
    print(-1)