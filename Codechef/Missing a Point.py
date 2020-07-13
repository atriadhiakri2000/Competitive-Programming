'''from collections import Counter
t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    x_cor=[]
    y_cor=[]
    for i in range(4*n-1):
        x,y=map(int,input().split())
        x_cor.append(x)
        y_cor.append(y)

    x_cor.sort()
    y_cor.sort()

    a=Counter(x_cor)
    b=Counter(y_cor)
    for i,j in a.items():
        if(j%2==1):
            n=i
    for i,j in b.items():
        if(j%2==1):
            m=i
    print(n,m)

1
2
1 1
1 2
4 6
2 1
9 6
9 3
4 3

'''
def solve():
    x=int(input())
    jason=[]
    tim=[]
    for s in range(4*x-1):
        c,d=map(int,input().split())
        jason.append(c)
        tim.append(d)
    alpha=Counter(jason)
    beta=Counter(tim)
    for m in alpha.keys():
        if(m%2!=0):
            ans=alpha[m]
    for n in beta.keys():
        if(n%2!=0):
            res=beta[n]
    print( ans,res)

from collections import Counter
t=int(input())
while(t>0):
    t=t-1
    solve()
