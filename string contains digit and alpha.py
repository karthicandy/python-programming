k1=(input())
x=0
y=0
for z in k1:
  if z.isalpha():
    x+=1
  elif z.isdigit():
    y+=1
if x>1 and y>1:
  print("Yes")
else:
  print("No")
