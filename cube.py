a=int(input())
sum=0
n=a
while((n//10)!=0):
    d=n%10
    sum=sum+pow(d,3)
    n=n//10 #store no in variable after div
sum=sum+pow(n,3)
if(sum==a):
    print("is armstrong")
else:
    print("not armstrong")

