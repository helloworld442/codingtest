N = list(input())
N.sort(reverse=True)
N = ''.join(N)
if N[-1] == '0' and int(N) % 30 == 0:
    print(''.join(N))
else:
    print(-1)