"""
num1=int(input("enter a number:"))
num2=int(input("enter a number:"))
result=num1+num2
print(result)

list=[2,5,4,5,5,4]
count5=list.count(5)
count4=list.count(4)
count2=list.count(2)
if (5 and 7)in list:
    print(list)
else:
    print("there is no ")
list.sort()
print(list)
print(len(list))

age=int(input("please enter you age:"))
if age>=50:
    print("alle kacabso akhiradaada ushaqayso ")
if age>20 and age<=49:
    print("aduniyo khiraba ku dadaal")
if age <=19:
    print("hada samee waxa madaxaaga kaguuxi si aadan hadho udhin hadaan samaynlaa haa waagii aan yaraa")

name =input("wha is your name? ")
color=input("what is yuor favatare color? ")
print(name + " like " + color)
 
 #calculating age
birth=int(input("please enter birth year "))
age=2021-birth
print(age)

#converting pounce into kg
w=int(input("please enter your weight as a pounce "))
kg=float(w/2.2046)
print(kg)

num=[5,2,5,2]
for a in num:
    print(" p"*a)
    """
def add_number(n1,n2):
    result=n1+n2
    print("the sum of numbers is ",result)

numner1=int(input("please enter a number"))
numner2=int(input("please enter a number"))
add_number(numner1,numner2)