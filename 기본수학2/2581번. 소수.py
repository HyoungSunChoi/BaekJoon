'''
자연수 M,N 이 주어질 때 M 이상 N 이하의 자연수 중 소수인 것을 골라 ,
이들의 합과 최솟값을 찾는 프로그램

ex.) 60 - 100
'''
m=int(input())
n=int(input())
lst=[i for i in range(m,n+1)]
sosu=[]
for i in lst:
    cnt=0
    if i==1:
        continue
    for x in range(2,i+1):
        if i%x==0:
            cnt+=1
    if cnt==1:
        sosu.append(i)
if len(sosu)>=1:
    print(sum(sosu))
    print(sosu[0])
else:
    print(-1)