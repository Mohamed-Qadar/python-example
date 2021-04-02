
#sida  xisaabaadka lagu sameyo python
print("sodhawow:")
while(True):
    print("\n\nfadlan  xisaabta aad doonihaysid  dooro\niskudar,kalajarid,isku dhufasho,isu qaybin,isku jabaar,")
    x=input()
    if(x=="iskudar"):
        a=int(input("raqamka koobaad gali:"))
        b=int(input("raqamka labaad gali:"))
        jawaab=a+b
        print(jawaab)
        print("inaad siiwado marabtaa(H/M)")
        q=input()
        if(q=="H"):
            continue
        else:
            print("waad ku guleysatay,malin wanaagsan,bye:")
            break
        
    elif(x=="kalajarid"):
      a=int(input("raqamka koobaad gali:"))
      b=int(input("raqamka labaad gali:"))
      jawaab=a-b
      print( jawaab)
      print("inaad siiwado marabtaa(H/M)")
      q=input()
      if(q=="H"):
            continue
      else:
            print("waad ku guleysatay,malin wanaagsan,bye:")
            break
    elif(x=="isku dhufasho"):
      a=int(input("raqamka koobaad gali:"))
      b=int(input("raqamka labaad gali:"))
      jawaab=a*b
      print( jawaab)
      print("inaad siiwado marabtaa(H/M)")
      q=input()
      if(q=="H"):
            continue
      else:
            print("waad ku guleysatay,malin wanaagsan,bye:")
            break 
    elif(x=="isu qaybin"):
      a=int(input("raqamka koobaad gali:"))
      b=int(input("raqamka labaad gali:"))
      jawaab=a/b
      print( jawaab)
      print("inaad siiwado marabtaa(H/M)")
      q=input()
      if(q=="H"):
            continue
      else:
            print("waad ku guleysatay,malin wanaagsan,bye:")
            break
    elif(x=="isku jabaar"):
        a=int(input("nambarka hoseyah ah qor:"))
        b=int(input("bawaka qor:"))
        jawaab=a**b
        print(jawaab)
        print("inaad siiwado marabtaa(H/M)")
        q=input()
        if(q=="H"):
            continue
        else:
            print("waad ku guleysatay,malin wanaagsan,bye:")
            break



    