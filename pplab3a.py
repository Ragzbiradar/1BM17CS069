def divisor(a):
    i=1
    arr=[]
    while i<=a:
        if a%i==0:
            arr.append(i)
        i=i+1
    print(arr)

n=int(input("enter the number"))
print("divisors are")
divisor(n)
