'''
정수 N 이 주어졌을 때 소인수 분해하는 프로그램을 작성하시오
'''
n=int(input())
while n!=1:
    for i in range(2,n+1):
        if n%i==0:
            print(i)
            n=n//i
            break

