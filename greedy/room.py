n = int(input())
time = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x:(x[1], x[0]))
print(time)