from collections import defaultdict
def minimal(list1,list2,x):
    list1.sort()
    list2.sort()
    list2.reverse()
    list3=list1.copy()
    list3=list3+list2
    value=min(list3)
    y=0
    for i in range(len(list1)):
        y=y+min(2*x,list1[i],list2[i])
    return(y)
def solution(x,y):
    q=defaultdict(int)
    w=defaultdict(int)
    e=defaultdict(int)
    for i in x:
        q[i]=q[i]+1
        w[i]=w[i]+1
    for i in y:
        q[i]+=1
        e[i]+=1
    odd=0
    miss1=[]
    miss2=[]
    for i in q:
        if(q[i]%2==1):
            odd=1
            break
        if(w[i]>e[i]):
            miss1.extend([i]*((w[i]-e[i])//2))
        elif(e[i]>w[i]):
            miss2.extend([i]*((e[i]-w[i])//2))
    if(odd):
        print(-1)
        return 1
    if(len(miss1)==0):
        print(0)
        return 1
    j=min(x+y)
    print(minimal(miss1,miss2,j))
t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    list1=list(map(int,input().rstrip().rsplit()))
    list2=list(map(int,input().rstrip().rsplit()))
    solution(list1,list2)
