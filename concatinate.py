list1=[]
list2=[]
n=int(input("Enter the no of elements in list1"))
for i in range(0,n):
    list1.append(int(input("Enter"+str(i) +"th number")))
n=int(input("Enter the no of elements in list2"))
for i in range(0,n):
    list2.append(int(input("Enter"+str(i)+"th number")))
print(list1+list2)


