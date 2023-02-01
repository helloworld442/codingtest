dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(x,y):
    global q,data,cnt
    while q:
        x,y = q.pop(0)
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if data[nx][ny] == '#':
                continue
            if data[nx][ny] == ".":
                #data[nx][ny] == "#"
                q.append((nx,ny))

    return cnt



#입력 받기
N,M = map(int,input().split())
data = [input()*M for _ in range(N)]
blue = []
red = []
hole = []
cnt = 0
#data 중에서 빨간공,파란공,구멍 따로 넣기
for i in range(N):
    for j in range(M):
        if data[i][j] == 'B':
            blue.append((i,j))
        elif data[i][j] == 'R':
            red.append((i,j))
        else:
            hole.append((i,j))

#red의 시작좌표 -> bfs
q = [(red[0][0],red[0][1])]
a = bfs(red[0][0],red[0][1])
cnt = 0
q = [(blue[0][0],blue[0][1])]
b = bfs(blue[0][0],blue[0][1])


# red 와 blue 가 같이 도착했는지 확인
if a == b:
    print(-1)
else:
    print(a)