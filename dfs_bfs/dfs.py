def dfs(index):
    global visit
    global graph
    visit[index] = True
    print(index, end = ' ')
    for next in range(N+1):
        if not visit[next] and graph[index][next]:
            dfs(next)
def bfs():
    global q,visit
    while q:
        cue = q.pop(0)
        print(cue,end = ' ')
        for next in range(1,N+1):
            if not visit[next] and graph[cue][next]:
                visit[next] = True
                q.append(next)
#입력 초기화
N,M,V = map(int,input().split())
#graph 설정
graph = [[False]*(N+1) for _ in range(N+1)]
visit = [False] * (N+1)
for _ in range(M):
    a,b = map(int,input().split())
    graph[a][b] = True
    graph[b][a] = True
#1.dfs
dfs(V)
print()
#2.bfs
visit = [False] * (N+1)
q = [V]
visit[V] = True
bfs()