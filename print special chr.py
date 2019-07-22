x=str(input())
count=0
for y in x:
    if y.isnumeric() or y.isalpha():
        pass
    else:
        count+=1
print(count)
