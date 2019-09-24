class Para:
    def __init__(self):
        self.open=[]
        self.close=[]
    def checkvalid(self,str):
        valid=False
        for each in str:
            if each == '(' or each=='{' or each== '[':
                self.open.append(each)
            elif each == ')' or each =='}' or each ==']' :
                self.close.append(each)
        print(self.open)
        print(self.close)
        if( len(self.open) != len(self.close)):
             valid = False
        else:
            for i in range (len(self.open)):
                    
                if self.open[i]=='(' and self.close[i]==')':
                     valid=True 
                elif self.open[i]=='{' and self.close[i]=='}':
                     valid=True
                elif self.open[i]=='[' and self.close[i]==']':
                     valid = True
                else:
                    valid = False

        if(valid):
            print("valid...")
        else:
            print("Invalid String...")

str=input("enter string")
Para().checkvalid(str)

            
                
