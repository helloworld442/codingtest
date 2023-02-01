a,b = map(int,input().split())
cnt = 1
while a != b:
    temp = b
    cnt += 1
    if b % 2 == 0:
        b = b // 2
    elif b % 10 == 1:
        b = b // 10
    else:
        print(-1)
        break


    if a > b:
        print(-1)
        break 
else:
    print(cnt)