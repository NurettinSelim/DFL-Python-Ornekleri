#İsim listeleri
kiz_isimler = ["fatma","ayşe","emine","hatice","zeynep","elif","meryem","şerife","zehra","sultan","hanife",
"merve","havva","zeliha","esra","fadime","özlem","hacer","melek","yasemin","rabia","hülya","cemile","sevim",
"gülsüm","leyla","dilek","büşra","aysel","songül","kübra","halime","esma","aynur","hayriye","kadriye","tuğba",
"sevgi","rukiye","hava","sibel","derya","filiz","asiye","keziban","ebru","ayşegül","döndü","selma","ayten"]

erkek_isimler = ["mehmet","mustafa","ahmet","ali","hüseyin","hasan","ibrahim","ismail","yusuf","osman","murat",
"ömer","ramazan","halil","süleyman","abdullah","mahmut","salih","recep","fatih","kadir","emre","mehmet ali",
"hakan","adem","kemal","yaşar","bekir","musa","metin","bayram","serkan","orhan","burak","furkan","yasin","gökhan",
"uğur","muhammed","yakup","muhammet","şükrü","enes","yunus","cemal","arif","onur","yılmaz","şaban","halil ibrahim"]

#kontrol değişkeni
yaygin = False


#Kullanıcıdan verilerin alınması
cinsiyet = input("Cinsiyetinizi giriniz(E/K):")
kullanici_isim = input("Adınızı küçük harflerle giriniz:")


if cinsiyet=="E":
    for isim in erkek_isimler:
        #Eğer listedeki bir isimle kullanıcının ismi eşleşirse
        if kullanici_isim == isim:
            yaygin = True
elif cinsiyet=="K":
    for isim in kiz_isimler:
        #Eğer listedeki bir isimle kullanıcının ismi eşleşirse
        if kullanici_isim == isim:
            yaygin = True


#Kullanıcıya geri dönüt
if yaygin == True:
    print("İsminiz({}) sık kullanılıyor".format(kullanici_isim.capitalize()))
elif yaygin == False:
    print("İsminiz({}) o kadar da sık kullanılmıyor".format(kullanici_isim.capitalize()))