#입력받기(-부호와 + 부호를 기점으로 나눠서 리스트)
data = input().split('-')
for i in range(len(data)):
    number = data[i].split('+')
    number = list(map(int,number))
    data[i] = sum(number)
data = list(map(int,data))
#+는 묶기 - 는 차례대로 빼기
n = data[0]
for i in range(1,len(data)):
    n -= data[i]
print(n)