#Listenin elemanlarının 7 ile tam bölünüp
#bölünmediğini kontrol eder

liste = [367, 893, 1267]

for sayi in liste:
    kalan = sayi % 7
    if kalan == 0:
        print(sayi,"7'ye tam bölünüyor")
    else:
        print(sayi, "7'ye bölümünden kalan", kalan)