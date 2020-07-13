t=int(input())
for j in range(t):
    count=0
    n=int(input())
    s=list(map(int,input().rstrip().rsplit()))
    for i in range(len(s)-1):
        count=count+abs(s[i+1]-s[i])-1
    print(count)
