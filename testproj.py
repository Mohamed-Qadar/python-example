num1=int(input("please enter a number:"))
num2=int(input("please enter a number:"))
sum=num1+num2
print(sum)
if sum<10:
    num1=int(input("please enter a number:"))
    num2=int(input("please enter b number:"))
    """if sum>10:
           sum=num2+num1
           print(sum)
           """
 
else:
    print("10 buyuktur:",sum)