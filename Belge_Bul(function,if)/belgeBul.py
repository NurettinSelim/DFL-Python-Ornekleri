#Karne ortalamanıza göre hangi belge 
#alacağınızı bulan fonksiyon
def belge_bul(puan):
    if puan < 0:
        return "0'dan küçük not olamaz!"
    elif puan < 50:
        return "Belge alamadınız."
    elif puan <= 85:
        return "Teşekkür belgesi aldınız."       
    elif puan <= 100:
        return "Takdir belgesi aldıın :)"
    elif puan > 100:
        return "100'den yüksek alamazsın"
    else:
        return "geçersiz giriş"
		
print(belge_bul(85))