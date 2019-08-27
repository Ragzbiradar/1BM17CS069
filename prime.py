def prime(n):
    flag =True
    for i in range (2,n//2 +1):
        if n%i==0:
            flag= False
            break
    return flag
        
            
m=int(input("enter the starting range"))
n=int(input("enter the ending range"))
for j in range (m,n+1):
    if prime(j):
        print(str(j)+",",end="")
                
