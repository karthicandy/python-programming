x,y=map(str,input().split())
if (len(x)<len(y)):
    print(y)
elif(len(x)>len(y)):
    print(x)
else:
    print(y or x)
