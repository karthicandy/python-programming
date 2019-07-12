x=int(input())
for y in range (2,x):
    if (x%y==0):
        print('no')
        break
    
else:
    print('yes')
