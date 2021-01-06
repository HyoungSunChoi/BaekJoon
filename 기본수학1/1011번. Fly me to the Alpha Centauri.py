'''
k 광년을 이동했을 때 k-1, k , k+1 광년만 이동가능함
'''
import math
for _ in range(int(input())):  # 총 반복 횟수
    x, y = map(int, input().split())
    cha=y-x
    if cha<=3:
        print(cha)
    else:
        n=int(math.sqrt(cha))
        if cha == n**2:
            print(2*n-1)
        elif n**2<cha<=n**2+n:
            print(2*n)
        else:
            print(2*n+1)