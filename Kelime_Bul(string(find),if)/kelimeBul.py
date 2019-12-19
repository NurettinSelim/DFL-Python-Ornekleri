#Metinde istenen kelimeyi arar.

##
##find(x) : x değerini baştan itibaren string içinde arar ve 
##bulursa ilk bulduğu indeksi döndürür. Bulamazsa "-1" değerini verir.
##

metin = "Bilişim Teknolojileri Dersi"
index = metin.find("Ders")

if index != -1:
    print("Ders kelimesi metinde geçiyor.")
else:
    print("Ders kelimesi metinde geçmiyor.")