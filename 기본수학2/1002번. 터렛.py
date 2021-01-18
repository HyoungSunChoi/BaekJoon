T=int(input())
for t in range(T):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    # 두 점 사이의 거리
    distance=((abs(x2-x1)**2)+(abs(y2-y1)**2))**0.5
    # 원의 반지름의 합
    rs=r1+r2
    rm=abs(r1-r2)

    # case 1. 두 점이 같은 경우
    if distance==0:
        if r1==r2:
            print(-1)
        else:
            print(0)
    # case 2. 두 점이 다른 경우
    else:
        # 두 점 사이의 거리보다 반지름간의 합이 짧은 경우
        if distance==rs or distance==rm:
            print(1)
        # 두 점 사이의 거리보다 반지름간의 합이 같은 경우
        elif distance<rs and distance>rm:
            print(2)
        # 두 점 사이의 거리보다 반지름의 합이 긴 경우
        else:
            print(0)
