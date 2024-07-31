import math

def luas_segi_empat(sisi):
    return sisi * sisi

def keliling_segi_empat(sisi):
    return 4 * sisi

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang + lebar)

def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def keliling_segitiga(sisi1, sisi2, sisi3):
    return sisi1 + sisi2 + sisi3

def luas_lingkaran(jari_jari):
    return math.pi * jari_jari * jari_jari

def keliling_lingkaran(jari_jari):
    return 2 * math.pi * jari_jari

def menu():
    print("Pilih bangun datar yang ingin dihitung:")
    print("1. Segi Empat")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    print("5. Keluar")

def hitung_segi_empat():
    sisi = float(input("Masukkan panjang sisi segi empat: "))
    print(f"Luas Segi Empat: {luas_segi_empat(sisi)}")
    print(f"Keliling Segi Empat: {keliling_segi_empat(sisi)}")

def hitung_persegi_panjang():
    panjang = float(input("Masukkan panjang persegi panjang: "))
    lebar = float(input("Masukkan lebar persegi panjang: "))
    print(f"Luas Persegi Panjang: {luas_persegi_panjang(panjang, lebar)}")
    print(f"Keliling Persegi Panjang: {keliling_persegi_panjang(panjang, lebar)}")

def hitung_segitiga():
    alas = float(input("Masukkan alas segitiga: "))
    tinggi = float(input("Masukkan tinggi segitiga: "))
    sisi1 = float(input("Masukkan sisi 1 segitiga: "))
    sisi2 = float(input("Masukkan sisi 2 segitiga: "))
    sisi3 = float(input("Masukkan sisi 3 segitiga: "))
    print(f"Luas Segitiga: {luas_segitiga(alas, tinggi)}")
    print(f"Keliling Segitiga: {keliling_segitiga(sisi1, sisi2, sisi3)}")

def hitung_lingkaran():
    jari_jari = float(input("Masukkan jari-jari lingkaran: "))
    print(f"Luas Lingkaran: {luas_lingkaran(jari_jari)}")
    print(f"Keliling Lingkaran: {keliling_lingkaran(jari_jari)}")

def main():
    while True:
        menu()
        pilihan = input("Pilih menu (1-5): ")
        if pilihan == '1':
            hitung_segi_empat()
        elif pilihan == '2':
            hitung_persegi_panjang()
        elif pilihan == '3':
            hitung_segitiga()
        elif pilihan == '4':
            hitung_lingkaran()
        elif pilihan == '5':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")

if __name__ == "__main__":
    main()
