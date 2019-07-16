am=int(input())
x=am
sum=0
while am>0:
    sum+=((am%10)**3)
    am=am//10
if (sum==x):
    print('yes')
else:
    print('no')
