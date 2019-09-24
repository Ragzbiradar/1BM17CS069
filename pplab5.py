class CallDetail:
    def __init__(self):
        self.dailer = None
        self.receiver = None
        self.duration = None
        self.calltype = None

    def set_details(self,y):
        self.dailer = y[0]
        self.receiver = y[1]
        self.duration = y[2]
        self.calltype = y[3]
        self.getdetails()
    def getdetails(self):
        print(self.dailer.ljust(20),end=" ")
        print(self.receiver.ljust(20),end=" ")
        print(self.duration.ljust(20),end=" ")
        print(self.calltype.rjust(20))
        
class util:
    def __init__(self):
        self.list_of_call_Objects= []

    def parse_customer(self,list_of_call_strig):
        for x in range(len(list_of_call_strig)):
            y=list_of_call_strig[x].split(",")
            #print(y)
            self.list_of_call_Objects.append(CallDetail())
            self.list_of_call_Objects[x].set_details(y)
            


call='9999012375,93330000104,23,STD'
call1='7418596301,7531234589,54,Local'
call2 = '9991110001,7531478965,6,ISD'
list_of_call_strig=[call,call1,call2]

print("Dailer".ljust(20),end=" ")
print("Receiver".ljust(20),end=" ")
print("Duration".ljust(20),end=" ")
print("Type".rjust(20))
util().parse_customer(list_of_call_strig)


