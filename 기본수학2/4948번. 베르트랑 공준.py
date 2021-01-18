'''
베르트랑 공준 : 임의의 자연수 n에 대하여 n 보다 크고, 2n 보다 작거나 같은 소수는 적어도 하나 ㅏ존재한다
10보다크고 20보다 작거나 같은 소수는 4개,
14보다크고 28보다 작거나 같은 소수는 3개
'''
def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i==0:
                return False
        return True

li=list(range(2,123456*2))
prime_li=list()         # 미리 소수인 배열을 형성
for i in li:
    if isPrime(i):
        prime_li.append(i)

while True:
    ans=0
    n=int(input())
    if n==0: break
    for i in prime_li:
        if n<i<=2*n:
            ans+=1
    print(ans)
