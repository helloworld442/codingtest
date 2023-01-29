'''
[1,2,3,4,5]
[1,3,5,4,2]

'''
n = int(input())
answer = []
for _ in range(n):
    m = int(input())
    data = list(map(int,input().split()))
    data.sort()
    result = 0
    for j in range(2,m):
        result = max(result,abs(data[j] - data[j-2]))
    answer.append(result)
for i in range(len(answer)):
    print(answer[i])