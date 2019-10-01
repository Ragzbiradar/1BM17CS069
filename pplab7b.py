for i in range(4):
    for j in range(13):
        if(j%4!=0 and j!=4):
            print("-",end="")
        else:
            print(" ",end="")
    print('')
    if i!=3:
        for k in range(13):
            if(k%4==0):
                print("|",end="")
            else:
                print(" ",end="")
        print("")
                    
    
