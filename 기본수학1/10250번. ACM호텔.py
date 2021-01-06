'''
호텔 정문으로부터 걸어서 가장 짧은 거리에 있는 방을 선호한다.
각 층에 W개의 방이 있는 H 층 건물이다.
엘리베이터는 가장 왼쪽에 있다.
방 번호는 YXX 나 YYXX 형태 ( Y는 층수, X는 엘리베이터로부터의 거리
N 번째로 도착한 손님에게 배정될 방 번호를 계산하는 프로그램
101 , 201 , 301, YY01 까지 채우고
102 , 202, 302, 쭉쭉쭉
'''
# T 테스트케이스
# H, W, N ( 층수, 각 층의 방 수, 몇 번째 손님?)
import math
for _ in range(int(input())):
    H,W,N=map(int,input().split())
    floor=(100*(N%H) if N%H!=0 else 100*H)
    hosu=N/H
    hosu=math.ceil(hosu)
    print(floor+hosu)