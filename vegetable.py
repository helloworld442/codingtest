import sys
sys.setrecursionlimit(10**9)
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def dfs(y,x):
    global visited
    visited[y][x] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if graph[ny][nx] == 1 and visited[ny][nx] == 0:
             dfs(ny,nx)
#입력 초기값
T = int(input())
for _ in range(T):
    M,N,K = map(int,input().split())#N = 가로, M = 세로 K = 배추 갯수
    graph = [[0]*(60) for _ in range(60)]
    visited = [[0]*(60) for _ in range(60)]
    for _ in range(K):
        x,y = map(int,input().split())
        #그래프 정보 입력
        graph[y+1][x+1] = 1
        #dfs
    count = 0
    for i in range(1,M+1):#가로
        for j in range(1,N+1):#세로
            if graph[j][i] == 1 and visited[j][i] == 0:
                dfs(j,i)
                count += 1
    print(count)