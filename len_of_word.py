n=int(input("enter the number of words:"))
list=[]
for i in range(n):
    x=input("enter the word:")
    list.append(x)
print(list)
max=len(list[0])
temp=list[0]
for i in list:
    if(len(i)>max):
        max=len(i)
        temp=i
print("the word havin longest length is:",temp,"and the length is",max)
