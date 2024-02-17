class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def kitap_listele(self):
        with open("books.txt", "r") as file:
            tutucu = file.readlines()

        for kitap in tutucu:
            kitap_bilgileri = kitap.split(",")

            print(f"Kitap: {kitap_bilgileri[0]}, Yazar: {kitap_bilgileri[1]}")
            print()
            
    def kitap_ekle(self):
        kitap_adi = input("Eklemek İstediğiniz Kitap Adı: ")
        yazar = input("Yazar: ")
        yayin_tarihi = input("Yayın Tarihi: ")
        sayfa_sayisi = input("Sayfa Sayısı: ")

        kitap_bilgileri = f"{kitap_adi},{yazar},{yayin_tarihi},{sayfa_sayisi}\n"

        with open("books.txt", "a") as file:
            print()
            file.write(kitap_bilgileri)
            
    def kitap_kaldir(self):
        kitap_adi = input("Kaldırmak İstediğiniz Kitap Adı: ")

        with open("books.txt", "r") as file:
            tutucu = file.readlines()

        kitap_bulundu = False
        for i, kitap in enumerate(tutucu):
            kitap_bilgileri = kitap.split(",")
            if kitap_adi == kitap_bilgileri[0]:
                kitap_bulundu = True
                silinecek_kitap_dizini = i
                break
    
        if not kitap_bulundu:
            print(f"{kitap_adi} adlı kitap bulunamadı.")
            return

        del tutucu[silinecek_kitap_dizini]

        with open("books.txt", "w") as file:
            file.truncate(0)

        with open("books.txt", "a") as file:
            for kitap in tutucu:
                file.write(kitap)
        print(kitap_adi, "adlı kitabı kaldırdınız...")
              
    def kitap_sayisi(self):
        with open("books.txt", "r") as file:
            tutucu = file.readlines()
        return len(tutucu)
            
    def __del__(self):
        self.file.close()


lib = Library()

while True:
    print("*** MENÜ***")
    print("1) Kitapları Listele")
    print("2) Kitap Ekle")
    print("3) Kitap Kaldır")
    print("4) Kitap Sayısı:")
    print("5) Çıkış")

    secim = input("Seçiminiz: ")
    print()

    if secim == "1":
        lib.kitap_listele()
    elif secim == "2":
        lib.kitap_ekle()
    elif secim == "3":
        lib.kitap_kaldir()
    elif secim == "4":
        print(lib.kitap_sayisi())
    elif secim == "5":
        break
    else:
        print("Geçersiz seçim.")