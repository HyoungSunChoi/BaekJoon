'''
두 명의 덩치가 (x,y) (a,b)  x>a, y>b 일 때 1, 2보다 크다.
키와 몸무게 하나만 큰 경우에는 크다고 말할 수 없다.
'''

res=list()
n=int(input())
for _ in range(n):
    a,b=map(int,input().split())
    res.append((a,b))

for i in res:
    rank=1
    for j in res:
        if i[0]<j[0] and i[1]<j[1]:
            rank+=1
    print(rank,end=' ')