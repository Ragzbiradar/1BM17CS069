class Student:
    def set_details(self):
        self.id=input("enter name")
        self.cie=[]
        print("enter 3 cie marks")
        for i in range(3):
            self.cie.append(int(input()))
        self.see=[]
        print("enter 3 see marks")
        for i in range(3):
            self.see.append(int(input()))
        self.total=[]
    def calculate(self):
        for i in range(3):
            self.total.append(self.see[i] + self.cie[i])
        self.sum1= sum(self.total)/3
        return self.sum1
s1=[]
marks=[]
pos=0
n=int(input("enter number of students"))
for i in range(n):
    s1.append(Student())
    s1[i].set_details()
    marks.append(s1[i].calculate())
grt=marks[i]
for i in range(1,n):
    if(grt<marks[i]):
        grt=marks[i]
        pos=i
print("the topper is :",s1[pos].id)


    
      
    
            
        
