print("""*******************************************

Atm Makinesine Hoşgeldiniz.

İşlemler:

1. Bakiye Sorgulama

2. Para Yatırma

3. Para Çekme

Programdan çıkmak için 'q' ya basın.

""")

bakiye=1000

while True:
    işlem = input("işlemi seçiniz:")
    if (işlem == "q"):
        print("Programdan çıkılıyor. Yine Bekleriz...")
        break
    elif (işlem=="1"):
        print("Bakiyeniz {} tldir.".format(bakiye))

    elif (işlem == "2"):
        miktar = int(input("Ne kadar para yatırmak istiyorsunuz?"))
        bakiye+= miktar

    elif (işlem == "3"):
        miktar = int(input("Ne kadar para çekme istiyorsunuz?"))
        if (miktar>bakiye):
            print("Yetersiz Bakiye!")
            continue
        bakiye-=miktar

    else:
        print("Geçersiz işlem!")
3