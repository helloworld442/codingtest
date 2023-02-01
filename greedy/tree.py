'''
[2,4,5,7,9]
[2,4,9,7,4]

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