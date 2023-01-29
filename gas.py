'''
4
2 3 1
5 2 4 1

'''

#입력 받기
n = int(input())
coin = list(map(int,input().split()))
gas = list(map(int,input().split()))
sum1 = 0
#gas 바구기
for i in range(len(coin)):
    #전엥 gas가 지금 gas 보다 작다면 
    if gas[i] <= gas[i+1]:
        gas[i+1] = gas[i]

    #요금 계산
    sum1 += (gas[i]*coin[i])
print(sum1) 