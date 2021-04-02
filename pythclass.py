"""
class Araba():
    marka=" "
    renk=" "
    palaka=" "
    uzunlugu=" "
    print()
araba1=Araba()
araba1.marka="byz"
araba1.renk="siyaha"
araba1.palaka="23 pa 34"
araba1.uzunlugu=35
araba2=Araba()
araba2.marka="mgn"
araba2.renk="RED"
araba2.uzunlugu=34
araba2.palaka="WR 123"
print("-------ARABA 1------")
print("Marka: {} \nRenk :{}\nPlaka :{} \nuzunlugu :{}".format(araba1.marka,araba1.renk,araba1. palaka,araba1.uzunlugu))

print("-------ARABA 2------")
print("Marka: {} \nRenk :{}\nPlaka :{} \nuzunlugu :{}".format(araba2.marka,araba2.renk,araba2. palaka,araba2.uzunlugu))
"""
import random

member=["moha farmajo","hasan","sheikh shariif"]
lider=random.choice(member)
print(lider)