T = int(input())

for i in range(T):
    R, S = input().split()
    txt = ""
    for i in S:
        txt += int(R) * i
    print(txt)