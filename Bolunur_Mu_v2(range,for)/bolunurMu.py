#1500 2000 aralığında 8'e bölünen sayıları bulur

for sayi in range(1500,2001):
    kalan = sayi % 8
    if kalan == 0:
        print(sayi,"8'e tam bölünüyor")
