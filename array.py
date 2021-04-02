a=int(input("enter your age: "))
if a>=65:
    print("stay your home,because of corona")
    print("do want to continue(Y/N)")
    ans=input()
    if (ans=="N"):
        a=int(input("enter your age: "))
elif a<50 and a>20:
    print("take cara you mask")
else:
    print("you are younge go where you ever want to go")