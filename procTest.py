print("oyuncu kaydetme program........")
ad=input("lutfen adinii girin:")
soyad=input("lutfen soyadinizi girin:")
takim=input("lutfen oynadiniz takim girin:")
bilgi=[ad,soyad,takim]
print("veriyi kaydedildi...")
print("girmis oldugunuz bilgiler sunlar oldugunu emin misiniz?(E/H)?")
cevap=input()
if cevap=="E":
    print("barisi lie gerceklestirildil")
else:
    print("bir daha girin:")
    continue