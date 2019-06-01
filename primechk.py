num=int(input())
for i in range(2,num+1):
    prime=True
    for k in range(2,i):
       if(i%k==0):
         prime=False
       break
    if(prime):
     print(i)
