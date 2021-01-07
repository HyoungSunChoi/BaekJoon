'''
N 장의 카드를 숫자가 보이도록 바닥에 놓는다
숫자 M 을 외친다
N 장의 카드 중 3장의 카드를 골라 M 을 넘지 않으면서 최대한 가까운 합을 구하라

첫째줄 카드 개수 N 과 M 이 주어진다.
둘째줄 카드에 쓰여있는 수가 주어진다

from itertools import permutations
n,m=map(int,input().split())
num_list=list(map(int,input().split()))
result=list(permutations(num_list,3))
res=0
for x in result:
    if sum(x)<=m:
        if res<sum(x):
            res=sum(x)
print(res)
'''
n,m=map(int,input().split())
a=list(map(int,input().split()))
biggest=0
for i in range(len(a)):
    for j in range((i+1),len(a)):
        for k in range((j+1),len(a)):
            c=a[i]+a[j]+a[k]
            if c>biggest and c<=m:
                biggest=c
print(biggest)