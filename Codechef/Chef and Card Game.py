def getSum(n):
    
    sum = 0
    while (n != 0): 
      
        sum = sum + int(n % 10) 
        n = int(n/10) 
      
    return (sum)
t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    chef=0
    morty=0
    for i in range(n):
        a,b=map(int,input().split())
        x=getSum(a)
        y=getSum(b)
        if(x>y):
            chef=chef+1
        elif(y>x):
            morty=morty+1
        else:
            morty=morty+1
            chef=chef+1

    if(chef>morty):
        print(0,chef)
    elif(chef<morty):
        print(1,morty)
    else:
        print(2,morty)
