s=input()
n=s.lstrip('-').replace('.','',1).isdigit()
if(n==True):
	print("yes")
else:
	print("No")
