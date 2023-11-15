a=int(input("A:"))
b=int(input("B:"))
operation=input("add/sub/mul/divi:")
if(operation=="add"):
    print(a+b)
elif(operation=="sub"):
    print(a-b)
elif(operation=="mul"):
    print(a*b)
elif(operation=="divi"):
    print(a/b)
else:
    print("invalid operation")