'''
M*N 크기의 보드. 어떤 정사각형은 검정, 나머지 흰색
8*8 체스판으로 만든다.
체스판은 검,흰이 번갈아져 칠해져 있어야 한다.

'''
n,m=map(int,input().split())
board=[list(input()) for _ in range(n)]
for _ in board:
    print(_)
dx=[1,0,-1,0]
dy=[0,1,0,-1]
cnt=0
for i in range(1,n-2):
    for j in range(1,n-2):
        if all(board[i][j]!=board[i+dx[k]][j+dy[k]] for k in range(4)):
            continue
        else:
            print(i,j,cnt, board[i][j])
            cnt+=1
print(cnt)