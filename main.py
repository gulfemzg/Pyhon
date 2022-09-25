"""
100 kişilik bir üniversitede geçme notu 50'dir.
Finalden 60'tan düşük alınırsa geçme notuna bakılmaksızın öğrenci kalır.
Vize %40, final %60 etkili.
Geçenlerin kalanlara oranını ekrana yazdır.
"""
kalan = 0
gecen = 0
oran = 1
ortalama = 0
ogrenciler = [1,2,3,4,5]

for o in ogrenciler:
    vize = input(str(o) + ". öğrencinin vize notu : ")
    final = input(str(o) + ". öğrencinin final notu : ")

    vize = float(vize)
    final = float(final)

    ortalama = float(vize)*0.4 + float(final)*0.6

    if final<60.0 or ortalama<50.0:
        kalan+=1

    elif ortalama>=50.0:
        gecen+=1

    o+=1
oran = float(gecen)/float(kalan)
yuzde = float(oran)*100
print("Geçen/Kalan : " + str(oran))
print("Geçen/Kalan yüzdesi : %" + str(yuzde))