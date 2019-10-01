import os
f1=open("happy.txt","r")
f2=open("prime.txt","r")
primeno=f2.read()
happyno=f1.read()
#print(primeno)
#print(happyno)
happy=happyno.split(" ")
prime=primeno.split(", ")
#print(happy)
#print(prime)
count=0
for each in happy:
    if each in prime:
        print(each)
        count +=1
print("count",count)
            


