'''
왜 어려운가
1. 0을 고정하면서 1을 0으로  1을 고정하면서 0을 1로 바꾸는 것을 컴퓨터에게 전달하기가 어려움
2. 다른 1이 오기전까지의 0 여러개를 0하나로 컴퓨터에게 전달하기가 어려움
'''
data = input()
count1 = 0 # 0->1로 바꾸는 횟수
count2 = 0 #1 -> 0로 바꾸는 횟수
if data[0] == '0':
    count1 += 1
else:
    count2 += 1
for i in range(len(data)-1):
    if data[i] !=  data[i+1]:
        if data[i+1] == '0':
            count1 += 1
        else:
            count2 += 1
print(min(count1,count2))