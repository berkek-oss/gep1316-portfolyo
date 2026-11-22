# Kullanıcıdan adını ve doğum yılını alıp yaşını hesaplayan program
from datetime import date

# Kullanıcıdan ad alınır
ad = input("Adınız nedir? ")

# Doğum yılı alınır
dogum_yili = int(input("Doğum yılınız nedir? "))

# Bu yıl bilgisayarın tarihinden alınır
bu_yil = date.today().year

# Kendi eklediğim kısım: doğum yılı gelecekteyse uyarı ver
if dogum_yili > bu_yil:
    print(f"Uyarı: {dogum_yili} henüz gelmedi {ad}! Lütfen geçerli bir doğum yılı gir.")
else:
    # Yaş = bu yıl - doğum yılı
    yas = bu_yil - dogum_yili
    # Kişiye özel karşılama mesajı yazdırılır
    print(f"Merhaba {ad}! Bu yıl {yas} yaşına giriyorsun. Hoş geldin!")
