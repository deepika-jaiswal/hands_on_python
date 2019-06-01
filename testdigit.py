s=input()
flag=True
try:
    d=int(s)
except:
    flag=False
finally:
    if(flag):
        print("all digit")
    else:
        print("not digit")

