computer_num = int(input())
pair_num = int(input())
pair = [[] for i in range(computer_num+1)]

visited = [0]*(computer_num+1)  # 방문 여부 체크

for i in range(pair_num):
    a, b = map(int, input().split())

    pair[a] += [b]
    pair[b] += [a]

def DFS(pair_num):
    visited[pair_num] = 1

    for nx in pair[pair_num]:
        if visited[nx] == 0:
            DFS(nx)

DFS(1)
print(sum(visited)-1)