k1=int(input())
k2=list(map(int,input().split()))
avg=0
for i in k2:
    avg=avg+i
avg=avg/k1
print(int(avg))
    
