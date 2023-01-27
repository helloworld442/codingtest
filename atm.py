n = int(input())
data = list(map(int,input().split()))
# 내림차순
data.sort()
sum1 = 0
for i in range(1,n+1):
    sum1 += sum(data[:i])
print(sum1)