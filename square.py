n=int(input("enter  the number of elements:"))
nlist=[]
for i in range(n):
    a=int(input("enter the numbers:"))
    nlist.append(a)
print("entered list",nlist)
sqr_list=[x**2 for x in nlist]
print("squared numbers:",sqr_list)