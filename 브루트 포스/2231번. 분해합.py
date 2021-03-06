'''
어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다.
어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다.
예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다.
따라서 245는 256의 생성자가 된다.
물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.

자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.
'''

# 1 번째 방법
n=int(input())
sp=n//2
flg=True
while sp<n:
    res = 0
    new_sp=str(sp)
    for i in new_sp:
        res+=int(i) # 각 자리수의 합
    res+=int(new_sp) # 각 자리수 + 원래 수의 합
    if res==n:
        print(new_sp)
        flg=False
        break
    else:
        sp+=1
if flg==True:
    print(0)


# 2번째 방법 파이썬스럽게 풀기
# 생성자
def creater(num):
    sum=0
    a=list(map(int,str(num)))
    for x in a:
        sum+=x
    sum+=num
    return sum
flg=True
n=int(input())
for i in range(n//2,n+1):
    if creater(i)==n:
        print(i)
        flg=False
        break
if flg==True:
    print(0)
