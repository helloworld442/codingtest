n,money = map(int,input().split())
data = [int(input()) for i in range(n)]
data.sort(reverse=True)
s=0
for idx,c in enumerate(data):
    if money >= data[idx]:
        s+=money//c
        money%=c
print(s+money)