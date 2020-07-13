def solution(popu,x):
    l=[]
    c=0
    for i in popu:
        if(i<=x//2):
            c=c+1
        else:
            l.append(i)
    l.sort()
    k=0
    day=0
    if(len(l)>0):
        max_l=max(l)
    while(k<len(l)):
        tmp=l[k]
        if(tmp<=x):
            x=tmp*2
            k=k+1
        elif(x<=max_l):
            x=x+x
        day=day+1
    return (day+c)
t=int(input())
while(t):
    t=t-1
    n,x=map(int,input().split())
    popu=list(map(int,input().rstrip().rsplit()))
    y=solution(popu,x)
    print(y)

