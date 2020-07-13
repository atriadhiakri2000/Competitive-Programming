t=int(input())
while(t>0):
    t=t-1
    board=[ 'X' for i in range(64)]
    n=int(input())
    if(n==0):
        x = [board[i:i + 8] for i in range(0, len(board), 8)]  
        for i in x:
            print(*i)
            
    else:
        for i in range(n):
            if(i==0):
                board[0]='O'
            elif(board[i]=='X'):
                board[i]='.'

        x = [board[i:i + 8] for i in range(0, len(board), 8)]
        for i in range(8):
            if(i%2==0):
                for j in range(8):
                    print(x[i][j],end='')
                print()
            else:
                x[i].reverse()
                for j in range(8):
                    print(x[i][j],end='')
                print()
