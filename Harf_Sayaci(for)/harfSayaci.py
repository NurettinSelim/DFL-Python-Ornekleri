#Kelimedeki istenen harften kaç tane 
#bulunduğunu for döngüsü ile bulma

metin = "Marmara"
sayac = 0

for harf in metin:
    if harf == "a":
        sayac += 1

print(metin,'kelimesindeki "a" harfi sayısı',sayac)