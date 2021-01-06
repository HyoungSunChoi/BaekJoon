'''
3kg 5kg 봉지가 있을때
가장 적게 봉지를 가져갈 수 있는 개수 출력하라
'''
item=int(input())
cnt=0
while item>=0:
    if item%5==0:
        cnt+=item//5
        print(cnt)
        break
    else:
        item-=3
        cnt+=1
        