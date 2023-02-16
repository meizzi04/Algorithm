import sys

input = sys.stdin.readline

T = int(input())

for i in range(T) :
    a, b = map(int, input().split())

    a = a % 10 # 맨 뒷자리 수로 비교하므로 10으로 나눴을 때의 나머지 값과 같음

    if a == 0 : # 10의 배수
        print(10)
    elif a == 1 or a == 5 or a == 6 :
        print(a)
    elif a == 4 or a == 9 :
        b = b % 2 # 짝수인지 홀수인지 판단
        if b == 1 : # 홀수
            print(a)
        else : # 짝수
            print((a*a)%10)
    else : # 반복되는 수가 4개인 경우(2, 3, 7, 8)
        b = b % 4
        if b == 0 :
            print((a**4) % 10)
        else :
            print((a**b) % 10)