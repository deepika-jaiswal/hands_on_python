l=[3,4,5,6,88,90]
maxn=l[0]
minn=l[0]
for i in l:
    if(i>maxn):
        maxn=i
    
    if(i<minn):
        minn=i
print("maximum value:"+str(maxn))
print("minimum value:"+str(minn))
print("difference:"+str(maxn-minn))

