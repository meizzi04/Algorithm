T = int(input())
for i in range(T):
    floor = int(input())
    room = int(input())

    num = [i for i in range(1, room+1)]

    for j in range(floor):
        for k in range(1, room):
            num[k] += num[k-1]

    print(num[-1])