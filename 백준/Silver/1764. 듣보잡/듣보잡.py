import sys

input = sys.stdin.readline

N, M = map(int, input().split())
no_listen = []
no_see = []

for i in range(N):
    no_listen.append(input())

for i in range(M):
    no_see.append(input())

people_list = list(set(no_listen) & set(no_see))
people_list.sort()

print(len(people_list))
for i in people_list:
    print(''.join(i), end='')