'''
a 층의 b 호에 살려면 자신의 아래 (a-1)층의 1호부터 b호까지
사람들의 수의 합만큼 사람들을 데려와 살아야 한다.
'''

for _ in range(int(input())):
    k=int(input())
    n=int(input())
    res=[i for i in range(1,n+1)]
    for i in range(k):
        for j in range(1,n):
            res[j]+=res[j-1]
    print(res[-1])