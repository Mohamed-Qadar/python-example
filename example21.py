
"""
n=int(input("Enter number: "))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Reverse of the number:",rev)

n=int(input("enter a number: "))
if n==0:
    print("the nummber you enter is zero ")
elif n<0:
    print("the nummber you enter is nagative and you enetr this number ",n)
else:
    print("the nummber you enter is pozitive and you enetr this number ",n)
"""
#Python Program to Take in the Marks of 5 Subjects and Display the Grade
n=int(input("please enter the number of subject :"))
    a=[]
    for i in range(0,n):
        sub=int(input("enter subjects :"))
        a.append(sub)
    av=sum(a)/n
    if av>=90:
        print(av)
        print("you get AA")

    elif av>=75:
        print(av)
        print("you get BA")
    elif av>=65:
        print(av)
        print("you get BB")
    elif av>=60:
        print(av)
        print("you get CC")
    else:
        print(av)
        print("you are failed")


