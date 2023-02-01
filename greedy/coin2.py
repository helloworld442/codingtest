'''
처음에는 시간초과가 걸림
#입력받기
n, money = map(int,input().split())
data = []
count = 0
for i in range(n):
    data.append(int(input()))
#데이터 올림차순 정리
data.sort(reverse=True)
i = 0
while money > 0:
    if money >= data[i]:
        money -= data[i]
        count += 1
    else:
        i += 1
print(count)

이유
이 문제의 시간복잡도를 확인했을때 O(N)인것을 알 수 있다
근데 여기서 들어온 동전의 수 보다 더 많은 계산이 들어가는 알고리즘인 것을 알 수 있다.
따라서 나누기의 정의인 몫과 나머지를 통해서 O(N)을 만족시킨 알고리즘을 작성했다.
'''















n,money = map(int,input().split())
data = [int(input()) for i in range(n)]
data.sort(reverse=True)
s=0
for idx,c in enumerate(data):
    if money >= data[idx]:
        s+=money//c
        money%=c
print(s+money)
