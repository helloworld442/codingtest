#ver1
'''
def dfs(idx):
    global visit,cnt
    cnt += 1
    visit[idx] = True
    for i in range(N+1):
        if not visit[i] and graph[idx][i]:
            dfs(i)
#입력 초기화
N = int(input())
M = int(input())
# 그래프 설정
graph = [[False]*(N+1) for _ in range(N+1)]
visit = [False] * (N+1)
cnt = 0
# dfs
for _ in range(M):
    a,b = map(int,input().split())
    graph[a][b] = True
    graph[b][a] = True
dfs(1)
print(cnt-1)
'''


#ver2
def bfs():
    global q,visit,cnt
    while q:
        cue = q.pop(0)
        cnt += 1
        for i in range(N+1):
            if not visit[i] and graph[cue][i]:
                q.append(i)
                visit[i] = True
                
#입력
N = int(input())
M = int(input())
#그래프 정보 입력
graph = [[False]*(N+1) for _ in range(N+1)]
visit = [False] * (N+1)
for _ in range(M):
    a,b = map(int,input().split())
    graph[a][b] = True
    graph[b][a] = True

q = [1]
visit[1] = True
cnt = 0
#bfs
bfs()
print(cnt-1)