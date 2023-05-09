import sys
input = sys.stdin.readline
N, M = map(int, input().split())
pokemon_num = {}
pokemon_name = {}

for i in range(N):
    name = input().strip()

    pokemon_num[i] = name
    pokemon_name[name] = i

for i in range(M):
    item = input().strip()
    if item.isdigit() == True:  # 입력값이 숫자인 경우
        print(pokemon_num[int(item)-1])
    else:   # 입력값이 문자인 경우
        print(pokemon_name[str(item)]+1)