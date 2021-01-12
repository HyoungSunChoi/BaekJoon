'''
문제 : 주어진 N 개 중 소수가 몇개인지 찾아서 출력하는 프로그램
'''
n=int(input())
a=list(map(int,input().split()))
total_cnt=0
for idx in a:
    cnt = 0
    if idx==1:
        continue
    for x in range(2,idx+1):
        if idx%x==0:
            cnt+=1
    if cnt==1:
        total_cnt+=1
print(total_cnt)