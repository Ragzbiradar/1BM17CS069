def search(lis,a):
    print(lis)
    if a in lis:
        return True
    else:
        return False

lis=[]
while True:
    a=int(input("enter the element ....-1 to stop"))
    if a!= -1:
        lis.append(a)
    else :
        break
b=int(input("enter the element to be searched"))
brr=search(lis,b)
if brr:
    print(str(b)+"found")
else:
    print("not found")
