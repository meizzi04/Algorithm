import sys

input = sys.stdin.readline

N = int(input())
member = dict()

for i in range(N):
    name, state = map(str, input().split())

    if state == "enter":
        member[name] = state
    else:
        del member[name]

member = sorted(member.keys(), reverse=True)

for i in member:
    print(i)