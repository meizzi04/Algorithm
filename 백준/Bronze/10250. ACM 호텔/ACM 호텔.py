T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())  # h=각 호텔의 층 수, w=각 층의 방 수, n=몇

    floor = N % H
    room_line = (N // H) + 1
    if floor == 0:
        floor = H
        room_line -= 1

    print(floor * 100 + room_line)