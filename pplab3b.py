import string
import random
def password(str1,num):
    for i in range(6):
        print (str1[random.randint(0,100)],end=" ")
str1=string.printable
print(str1)
print(len(str1))

