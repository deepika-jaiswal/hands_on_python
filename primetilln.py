num=int(input())
for n in range(2,num+1):
    prime=True
    for k in range(2,n):
        if(n%k==0):
         prime=False
        break
    if(prime):
     print(n)
