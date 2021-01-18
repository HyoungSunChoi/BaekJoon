'''
2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다. -> 골드바흐 수
'''
def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True
prime_lst=[i for i in range(2,10000) if isPrime(i)]
def sosu(num):
    res_lst = list()
    a = b = 0
    min = 9999
    for x in range(2, n + 1):
        if x in prime_lst:
            res_lst.append(x)
    for i in range(len(res_lst)):
        for j in range(len(res_lst)):
            if res_lst[i] + res_lst[j] == n:
                if abs(res_lst[j] - res_lst[i]) < min:
                    min = res_lst[j] - res_lst[i]
                    a = res_lst[i]
                    b = res_lst[j]
    print(a, b)

T=int(input())
for _ in range(T):
    n=int(input())
    sosu(n)



sosu=[0 for i in range(10001)]
sosu[1]=1
for i in range(2,98):
    for j in range(i*2,10001,i):
        sosu[j]=1 # 일반수 구분
t= int(input())
for i in range(t):
    a=int(input())
    b=a//2
    for x in range(b,1,-1):
        if sosu[a-x]==0 and sosu[x]==0:
            print(x,a-x)
            break


