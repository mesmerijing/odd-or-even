print("Give two numbers")
x=int(input("number x "))
y=int(input("number y "))
if (x%2==0):
    print(str(x) + " is even")
else:
    print(str(x) + " is odd")
if (y%2==0):
    print(str(y) + " is even")
else:
    print(str(y) + " is odd")
if (x%4==0):
    print(str(x)+ " is a multiple of 4")
else:
    print(str(x)+ " is not a multiple of 4")
if (y%4==0):
    print(str(y)+ " is a multiple of 4")
else:
    print(str(y)+ " is not a multiple of 4")    
print("Give another two numbers")
num=int(input("number num "))
check=int(input("number check "))
if (check/num!=0):
    print("The two numbers you gave divide equally :)")
else:
    print("The two numbers you gave cannot divide equally :(")
