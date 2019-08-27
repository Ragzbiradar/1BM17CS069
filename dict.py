dict ={}
m=int(input("enter the nuber of entries"))
for i in range(m):
    sub=input("enter sub")
    cgpa=float(input("enter cgpa"))
    dict.update({sub:cgpa})
for s,c in dict.items():
    if c>9.0:
        print(str(s)+","+str(c))
        
