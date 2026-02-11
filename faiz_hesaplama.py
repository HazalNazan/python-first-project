ana_para = float(input("Ana para miktarını girin: "))
faiz_orani = float(input("Yıllık faiz oranını girin (%): "))
sure = int(input("Kaç yıl vadeli: "))

faiz = ana_para * (faiz_orani / 100) * sure
toplam = ana_para + faiz

print("Kazanılan faiz:", faiz)
print("Vade sonu toplam para:", toplam)
