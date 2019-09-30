class Para:
    def __init__(self):
        self.open=[]
        self.i=None
    def checkvalid(self,str):
        valid=False
        for each in str:
            if each == '(' or each=='{' or each== '[':
                self.open.append(each)
               # print("list",self.open)
            elif each == ')' or each=='}' or each== ']':
                if len(self.open) !=0 :
                    self.i = self.open.pop()
                   # print("poped",self.i)
                else:
                    self.i=None
                if each == ')' and  self.i == '(':
                    valid=True
                elif each == '}' and  self.i=='{':
                    valid =True
                elif each == ']' and  self.i =='[':
                    valid = True
                else:
                    valid =False
       # if len(self.open) !=0 :
         #    valid =False
        if(valid):
            print("valid string...")
        else:
            print("Invalid String...")

str=input("enter string")
Para().checkvalid(str)

            
                
