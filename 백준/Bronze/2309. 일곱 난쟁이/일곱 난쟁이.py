height = []

for i in range(9) :
    height.append(int(input()))

for i in height :
    for j in height :
        if sum(height) - i - j == 100 and i != j :
            height.remove(i)
            height.remove(j)

height.sort() # 오름차순으로 정렬

for i in height :
    print(i)