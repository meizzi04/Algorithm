N = int(input())
score = list(map(int, input().split()))

max = max(score)

score_list = []

for i in score :
    score_list.append(i/max*100)

print(sum(score_list)/N)