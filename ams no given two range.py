x,y=map(int,input().split())
for i in range(x+1,y):
    sum=0
    z=i
    while i>0:
        sum+=((i%10)**3)
        i=i//10
    if (sum==z):
        print(sum,end=' ')
