yapilacaklar = []

while True:
    komut = input("Göster, ekle, düzenle, tamamla ya da çıkış yazınız: ")
    komut = komut.strip()

    match komut:
        case 'ekle':
            yapilacak = input("Yapılacak listesine ekleme yapınız: ") + "\n"

            file = open('yapilacaklar.txt', 'r')
            yapilacaklar = file.readlines()
            file.close()

            yapilacaklar.append(yapilacak)

            file = open('yapilacaklar.txt', 'w')
            file.writelines(yapilacaklar)
        case 'göster':
            for index, item in enumerate(yapilacaklar):
                row = (f"{index + 1}-{item}")
                print (row)
        case 'edit':
            numara = int(input("Düzenlenecek numarayı giriniz: "))
            numara = numara - 1
            yeni_yapilacak = input("Yeni girdi yazınız: ")
            yapilacaklar[numara] = yeni_yapilacak

        case 'çıkış':
            break

        case 'tamamla':
            numara = int(input("Tamamlanacak görevin numarasını giriniz: "))
            yapilacak.pop(numara)

print("Hoşçakal!")
