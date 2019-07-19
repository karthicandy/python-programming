num=int(input())
lis=[]
for k in range(num):
	c=input()
	lis.append(c)
kar=[]
for k in zip(*lis):
	if(k.count(k[0])==len(k)):
		kar.append(k[0])
	else:
		break
print("".join(kar))
