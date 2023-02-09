import sys

M = int(sys.stdin.readline())
S = set() # 집합

for i in range(M) :
    arr = sys.stdin.readline().split()

    text = arr[0]

    if len(arr) == 1 :
        if text == "all" :
            S = set(s for s in range(1, 21))
        elif text == "empty" :
            S = set()
    else :
        x = int(arr[1])
        
        if text == "add" :
            S.add(x)
        elif text == "remove" :
            S.discard(x)
        elif text == "check" :
            if x in S :
                print(1)
            else :
                print(0)
        elif text == "toggle" :
            if x in S :
                S.discard(x)
            else :
                S.add(x)