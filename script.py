filmler : list[str] = []

def film_ekle(film:str) -> None:
    filmler.append(film)
    print(f"{film} listeye eklendi.")

def filmleri_goster() -> None:
    if not filmler:
        print("Film listesi boş.")
    else:
        print("Film Listesi:")
        for film in filmler:
            print(f"- {film}")

def film_ara(film:str) -> None:
    if film.lower() in [f.lower() for f in filmler]:
        print(f"{film} listede bulundu")
    else:
        print(f"{film} listede bulunamadı.")

def film_sil(film:str) -> None:
    if film.lower() in [f.lower() for f in filmler]:
        filmler.remove(film)
        print(f"{film} listeden silindi.")
    else:
        print(f"{film} listede bulunamadı.")

while True:
    print("Film Listesi Uygulaması\n")
    print("1. Film Ekle")
    print("2. Filmleri Göster")
    print("3. Film Ara")
    print("4. Film Sil")
    print("5. Çıkış")

    secim : str = input("Seçiminizi yapın (1-5): ")
    match secim:
        case "1":
            film = input("Eklemek istediğiniz filmin adını girin: ")
            if not film.strip():
                print("Film adı boş olamaz. Lütfen geçerli bir film adı girin.")
                continue
            film_ekle(film)
        case "2":
            filmleri_goster()
        case "3":
            film = input("Aramak istediğiniz filmin adını girin: ")
            if not film.strip():
                print("Film adı boş olamaz. Lütfen geçerli bir film adı girin.")
                continue
            film_ara(film)
        case "4":
            film = input("Silmek istediğiniz filmin adını girin: ")
            if not film.strip():
                print("Film adı boş olamaz. Lütfen geçerli bir film adı girin.")
                continue
            film_sil(film)
        case "5":
            print("Uygulamadan çıkılıyor...")
            break
        case _:
            print("Geçersiz seçim. Lütfen 1-5 arasında bir sayı girin.")