n = int(input())
data1= list(map(int,input().split()))
data2= list(map(int,input().split()))
data1.sort(reverse=True)
data2.sort()
sum1 = 0
for i in range(n):
    sum1 += (data1[i]*data2[i])
print(sum1)
