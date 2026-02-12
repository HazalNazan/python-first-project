# Yatırım getiri simülatörü

print("Yatırım Getiri Simülatörüne Hoş Geldiniz")

baslangic = float(input("Başlangıç yatırım tutarı: "))
aylik_ekleme = float(input("Her ay eklenecek tutar: "))
yillik_faiz = float(input("Yıllık faiz oranı (%): "))
yil = int(input("Kaç yıl yatırım yapacaksınız: "))

ay_sayisi = yil * 12
aylik_faiz = yillik_faiz / 100 / 12

toplam_para = baslangic

for ay in range(ay_sayisi):
    toplam_para = toplam_para * (1 + aylik_faiz)
    toplam_para = toplam_para + aylik_ekleme

print("Yatırım süresi sonunda toplam paranız:", round(toplam_para, 2))
