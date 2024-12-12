n=int(input("enter the number of elements in the list"))
list=[]
for x in range(n):
    x=int(input("enter the elements:"))
    if x<100:
        list.append(x)
    else:
        list.append('over')
print(list)