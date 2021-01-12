'''
M이상 N 이하의 모든 소수를 출력하라
'''
# 거듭제곱근 까지만 계산하기
def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i==0:
                return False
        return True

n,m=map(int,input().split())
a=[i for i in range(n,m+1) if isPrime(i)==True]
for _ in a:
    print(_)

