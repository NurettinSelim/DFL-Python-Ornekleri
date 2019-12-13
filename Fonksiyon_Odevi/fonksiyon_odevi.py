def belge_bul():
    puan = int(input("Karne ortalamanızı girin:"))
    if puan < 0:
        print("0'dan küçük not olamaz!")
    elif puan < 50:
        print("Belge alamadınız.")
    elif puan <= 85:
        print("Teşekkür belgesi aldınız.")        
    elif puan <= 100:
        print("Takdir belgesi aldıın :)")
    elif puan > 100:
        print("100'den yüksek alamazsın")
    else:
        print("geçersiz giriş")

def harflere_ayir(kelime):
    for harf in kelime:
        print(harf)

def tekrarla(ad):
    a=0
    while a < 10:
        a = a + 1
        print(ad)

belge_bul()

harflere_ayir("fonksiyonlar")

tekrarla("Nurettin")