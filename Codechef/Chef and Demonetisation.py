t=int(input())
while(t>0):
    t=t-1
    s,n=map(int,input().rsplit())
    c=0
    if(s==1):
        print(1)
    else:
        c=s//n
        x=s%n
        if(x==0):
            print(c)
        elif(x==1):
            print(c+1)
        elif(x>0 and x%2==0):
            print(c+1)
        else:
            print(c+2)
