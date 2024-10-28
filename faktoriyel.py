print("""
      ***************

Faktoriyel bulma çalışmasına hoşgeldiniz...

      ***************
      """)

sayı=int (input("Faktörüyelini öğrenmek istediğiniz sayıyı girin: "))

def faktoriyel(sayı):
    faktoriyel=1
    if (sayı==0 or sayı==1):
        return 1
    else:
        while(sayı>1):
            faktoriyel*=sayı
            sayı-=1
        return faktoriyel
sonuc = faktoriyel(sayı)
print(f"Sonuç: {sonuc}")
