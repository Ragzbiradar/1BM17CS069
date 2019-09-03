class Student:
    def __init__(self):
        self.stuid=None
        self.age=None
        self.marks=None
    def setter(self):
        self.stuid=input("enter student id")
        self.age=int(input("age:"))
        self.marks=int(input("marks in exam:" ))
    def validate_marks(self):
        if (self.marks>0 and self.marks<=100):
            return True
        else:
            return False
    def validate_age(self):
        if (self.age>20):
            return True
        else:
            return False
    def check_qualification(self):
        if(self.validate_marks() and self.validate_age()):
            if(self.marks>= 65):
                return True
            else:
                return False
        else:
            return False
    def getter(self):
        print("student Id:",self.stuid)
        print("age:",self.age)
        print("marks:",self.marks)
        if(s1.check_qualification()):
            print("student is elgible for university")
        else:
            print("not eligible for university")
        
s1=Student()
s1.setter()
s1.getter()

        
