# qor program 1 ila 100 inta udhaxaysa  3 iyo 5 markii la isku dhufto numberada ku jira so hilhaya
total=0
for i in (list(range(1,100))):
    if (i % 3 ==0 and i % 5 ==0):
        total +=i
        print(i)
print(total)