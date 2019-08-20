def fun(arr):
    b=[]
    print("even number in the are")
    for i in arr:
        if i%2==0:
            b.append(i)
    print(b)

arr=[]
n=int(input("enter the size of of list"))
print("enter the list elements ")
for x in range(n):
    item =int(input())
    arr.append(item)
print("given list :"+str(arr))
fun(arr)
