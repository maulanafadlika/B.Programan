import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def input_data_mahasiswa():
    cls()
    mahasiswa = []
    jumlah = int(input("Masukkan jumlah mahasiswa: "))
    for i in range(jumlah):
        nama = input(f"Masukkan nama mahasiswa ke-{i+1}: ")
        nim = input(f"Masukkan NIM mahasiswa ke-{i+1}: ")
        prodi = input(f"Masukkan Prodi mahasiswa ke-{i+1}: ")
        nilai = float(input(f"Masukkan nilai mahasiswa ke-{i+1}: "))
        mahasiswa.append({'nama': nama, 'nim': nim, 'prodi': prodi, 'nilai': nilai})
    return mahasiswa

def tampilkan_data_mahasiswa(mahasiswa):
    cls()
    print("Data Mahasiswa:")
    for m in mahasiswa:
        print(f"Nama: {m['nama']}, NIM: {m['nim']}, Prodi: {m['prodi']}, Nilai: {m['nilai']}")

def hitung_rata_rata_nilai(mahasiswa):
    if not mahasiswa:
        return 0
    total_nilai = sum(m['nilai'] for m in mahasiswa)
    return total_nilai / len(mahasiswa)

def cari_mahasiswa_nilai_tertinggi_dan_terendah(mahasiswa):
    if not mahasiswa:
        return None, None
    mahasiswa_tertinggi = max(mahasiswa, key=lambda x: x['nilai'])
    mahasiswa_terendah = min(mahasiswa, key=lambda x: x['nilai'])
    return mahasiswa_tertinggi, mahasiswa_terendah

def input_data_barang(barang):
    cls()
    jumlah = int(input("Masukkan jumlah barang: "))
    for i in range(jumlah):
        nama = input(f"Masukkan nama barang ke-{i+1}: ")
        kode = input(f"Masukkan kode barang ke-{i+1}: ")
        jumlah_barang = int(input(f"Masukkan jumlah barang ke-{i+1}: "))
        barang.append({'nama': nama, 'kode': kode, 'jumlah': jumlah_barang})
    return barang

def tampilkan_data_barang(barang):
    cls()
    print("Data Barang:")
    for b in barang:
        print(f"Nama: {b['nama']}, Kode: {b['kode']}, Jumlah: {b['jumlah']}")

def cari_barang_berdasarkan_kode(barang, kode):
    cls()
    for b in barang:
        if b['kode'] == kode:
            return b
    return None

def hapus_barang_berdasarkan_kode(barang, kode):
    cls()
    for b in barang:
        if b['kode'] == kode:
            barang.remove(b)
            return True
    return False

def input_data_transaksi():
    cls()
    transaksi = []
    jumlah = int(input("Masukkan jumlah transaksi: "))
    for i in range(jumlah):
        jenis = input(f"Masukkan jenis transaksi ke-{i+1} (pemasukan/pengeluaran): ")
        jumlah_transaksi = float(input(f"Masukkan jumlah transaksi ke-{i+1}: Rp. "))
        transaksi.append({'jenis': jenis, 'jumlah': jumlah_transaksi})
    return transaksi

def tampilkan_data_transaksi(transaksi):
    cls()
    print("Data Transaksi:")
    for t in transaksi:
        print(f"Jenis: {t['jenis']}, Jumlah: Rp. {t['jumlah']},-")

def hitung_total_pemasukan(transaksi):
    return sum(t['jumlah'] for t in transaksi if t['jenis'] == 'pemasukan')

def hitung_total_pengeluaran(transaksi):
    return sum(t['jumlah'] for t in transaksi if t['jenis'] == 'pengeluaran')

def hitung_saldo_akhir(transaksi):
    pemasukan = hitung_total_pemasukan(transaksi)
    pengeluaran = hitung_total_pengeluaran(transaksi)
    return pemasukan - pengeluaran

def menu():
    cls()
    print("Menu:")
    print("1. Data Mahasiswa")
    print("2. Inventaris Barang")
    print("3. Pengelolaan Keuangan Pribadi")
    print("0. Keluar")

def sub_menu_mahasiswa():
    cls()
    print("Sub-Menu Data Mahasiswa:")
    print("1. Input data mahasiswa")
    print("2. Tampilkan data mahasiswa")
    print("3. Hitung rata-rata nilai mahasiswa")
    print("4. Cari mahasiswa dengan nilai tertinggi dan terendah")
    print("0. Kembali ke menu utama")

def sub_menu_barang():
    cls()
    print("Sub-Menu Inventaris Barang:")
    print("1. Input data barang")
    print("2. Tampilkan data barang")
    print("3. Cari barang berdasarkan kode")
    print("4. Hapus barang berdasarkan kode")
    print("0. Kembali ke menu utama")

def sub_menu_keuangan():
    cls()
    print("Sub-Menu Pengelolaan Keuangan Pribadi:")
    print("1. Input data transaksi")
    print("2. Tampilkan data transaksi")
    print("3. Hitung total pemasukan")
    print("4. Hitung total pengeluaran")
    print("5. Hitung saldo akhir")
    print("0. Kembali ke menu utama")

def main():
    mahasiswa = []
    barang = []
    transaksi = []

    while True:
        menu()
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            while True:
                sub_menu_mahasiswa()
                sub_pilihan = input("Pilih sub-menu: ")
                if sub_pilihan == "1":
                    mahasiswa = input_data_mahasiswa()
                elif sub_pilihan == "2":
                    tampilkan_data_mahasiswa(mahasiswa)
                elif sub_pilihan == "3":
                    rata_rata = hitung_rata_rata_nilai(mahasiswa)
                    print(f"Rata-rata nilai mahasiswa: {rata_rata}")
                elif sub_pilihan == "4":
                    tertinggi, terendah = cari_mahasiswa_nilai_tertinggi_dan_terendah(mahasiswa)
                    print(f"Mahasiswa dengan nilai tertinggi: {tertinggi}")
                    print(f"Mahasiswa dengan nilai terendah: {terendah}")
                elif sub_pilihan == "0":
                    break
                else:
                    print("Pilihan tidak valid.")
                input("Tekan Enter untuk melanjutkan...") 
        elif pilihan == "2":
            while True:
                sub_menu_barang()
                sub_pilihan = input("Pilih sub-menu: ")
                if sub_pilihan == "1":
                    barang = input_data_barang(barang)
                elif sub_pilihan == "2":
                    tampilkan_data_barang(barang)
                elif sub_pilihan == "3":
                    kode = input("Masukkan kode barang yang dicari: ")
                    hasil = cari_barang_berdasarkan_kode(barang, kode)
                    if hasil:
                        print(f"Barang ditemukan: {hasil}")
                    else:
                        print("Barang tidak ditemukan.")
                elif sub_pilihan == "4":
                    kode = input("Masukkan kode barang yang akan dihapus: ")
                    if hapus_barang_berdasarkan_kode(barang, kode):
                        print("Barang berhasil dihapus.")
                    else:
                        print("Barang tidak ditemukan.")
                elif sub_pilihan == "0":
                    break
                else:
                    print("Pilihan tidak valid.")
                input("Tekan Enter untuk melanjutkan...")
        elif pilihan == "3":
            while True:
                sub_menu_keuangan()
                sub_pilihan = input("Pilih sub-menu: ")
                if sub_pilihan == "1":
                    transaksi = input_data_transaksi()
                elif sub_pilihan == "2":
                    tampilkan_data_transaksi(transaksi)
                elif sub_pilihan == "3":
                    total_pemasukan = hitung_total_pemasukan(transaksi)
                    print(f"Total pemasukan: Rp. {total_pemasukan},-")
                elif sub_pilihan == "4":
                    total_pengeluaran = hitung_total_pengeluaran(transaksi)
                    print(f"Total pengeluaran: Rp. {total_pengeluaran},-")
                elif sub_pilihan == "5":
                    saldo_akhir = hitung_saldo_akhir(transaksi)
                    print(f"Saldo akhir: Rp. {saldo_akhir},-")
                elif sub_pilihan == "0":
                    break
                else:
                    print("Pilihan tidak valid.")
                input("Tekan Enter untuk melanjutkan...")
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid.")
        input("Tekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()
