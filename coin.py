n = int(input())
money = 1000-n
data = [500,100,50,10,5,1]
cnt = 0
i = 0
while money > 0:
    if money >= data[i]:
        money -= data[i]
        cnt += 1
    else:
        i += 1
print(cnt)


'''
이문제를 더 간단하고 시간복잡도가 낮은 방식으로 풀어보자!

'''
