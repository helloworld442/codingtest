dx = [1,-1,0,0]
dy  = [0,0,1,-1]
def dfs(x,y):
    global count
    graph[x][y] = 0
    count += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < N and 0 <= ny < N:
            if graph[nx][ny] == 1:
                dfs(nx,ny)
#입력 받기
N = int(input())
graph = []
count_list = []
for _ in range(N):
    # 그래프 정보 입력
    graph.append(list(map(int,input())))
#dfs
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            count = 0
            dfs(i,j)
            count_list.append(count)

count_list.sort()
print(len(count_list))
for i in range(len(count_list)):
    print(count_list[i])
