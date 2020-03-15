'''
import random
import string
password = "zzpyxxxxx"
def randomString(stringLength=4):
 
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

a= randomString() 

while a!= password:
    a= randomString()
    f= open("passwords.txt","a")
    f.write(a,)
    f.write("\r\n")
'''
password ="zzpy"
with open("passwords.txt","r") as passwords:
    for i in passwords:
        stripper= i.strip()

        a = stripper
        if stripper==password:
            print("yay")
        else:
            pass


