a=input()
flag=True
try:
    for i in a:
        d=int(i)
except:
    flag=False
finally:
    if(flag):
        print("the string contains all digits")
    else:
        print("the string does not contains all digits")


