n = int(input())
c = [0]*3

while n > 0:
    if n >= 300:
        n -= 300
        c[0] += 1
    elif n >= 60:
        n -= 60
        c[1] += 1
    else:
        n -= 10
        c[2] += 1
if n != 0:
    print(-1)
else:
    print(*c)