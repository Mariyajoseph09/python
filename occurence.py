a=int(input("enter the number of elements:\n"))
li=[]
c=0
for i in range(a):
    x=input("enter the word")
    li.append(x)
for i in li:
    for j in i:
            if "a" in j.lower():
                c=c+1
print("the occurrence of a is",c)
