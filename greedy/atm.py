n = int(input())
data = list(map(int,input().split()))
# 내림차순
data.sort()
sum1 = 0
for i in range(1,n+1):
    sum1 += sum(data[:i])
print(sum1)

'''
그리디 알고리즘을 푸는데 가장 기본이 되는 아이디어가 내림차순,올림차순이다.
따라서 데이터를 올림차순으로 배치한다음에 차례대로 더하는 알고리즘을 작성했다.


'''
