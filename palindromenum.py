n=int(input())
c=0
b=n
while(n>0):
    n=n//10
    c=c+1
num=0
while(b>0):
    d=b%10
    b=b//10
    num=num+(d*pow(10,c-1))
    c=c-1
print(num)

