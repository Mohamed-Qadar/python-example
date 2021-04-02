"""
i=1
while(i<=5):
  j=1
  while(j<=5):
    print("#",end="")
    j=j+1
  i=i+1
  print()

for a in range(1,100):
  if a%5 !=0 or a%3 !=0:
    print(a)
 """ 



import math
for i in range(1,500):
    a=math.sqrt(i)
    if i%a==0:
        print(i, end=' ')