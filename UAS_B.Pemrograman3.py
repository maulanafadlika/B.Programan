import math

# Data barang akan disimpan dalam dictionary
data_barang = {}

def input_barang():
    nama_barang = input("Masukkan Nama Barang: ")
    harga = float(input("Masukkan Harga Barang: "))
    stok = int(input("Masukkan Stok Barang: "))
    data_barang[nama_barang] = {'harga': harga, 'stok': stok}
    print("Data barang berhasil diinput.")

def tampil_barang():
    if not data_barang:
        print("Tidak ada data barang.")
        return
    print("Data Barang:")
    print(f"{'Nama Barang':<20} {'Harga':<10} {'Stok':<10}")
    for nama, info in data_barang.items():
        print(f"{nama:<20} {info['harga']:<10} {info['stok']:<10}")

def hapus_barang():
    nama_barang = input("Masukkan Nama Barang yang ingin dihapus: ")
    if nama_barang in data_barang:
        del data_barang[nama_barang]
        print("Data barang berhasil dihapus.")
    else:
        print("Barang tidak ditemukan.")

def cari_barang():
    nama_barang = input("Masukkan Nama Barang yang dicari: ")
    if nama_barang in data_barang:
        info = data_barang[nama_barang]
        print(f"Nama Barang: {nama_barang}")
        print(f"Harga: {info['harga']}")
        print(f"Stok: {info['stok']}")
    else:
        print("Barang tidak ditemukan.")

def hitung_pembelian():
    if not data_barang:
        print("Tidak ada data barang.")
        return

    nama_barang = input("Masukkan Nama Barang yang dibeli: ")
    if nama_barang not in data_barang:
        print("Barang tidak ditemukan.")
        return

    jumlah_beli = int(input("Masukkan Jumlah yang dibeli: "))
    if jumlah_beli > data_barang[nama_barang]['stok']:
        print("Stok tidak cukup.")
        return

    harga_barang = data_barang[nama_barang]['harga']
    total_harga = harga_barang * jumlah_beli
    data_barang[nama_barang]['stok'] -= jumlah_beli

    print(f"Total Pembelian: {total_harga}")
    print(f"Stok Setelah Pembelian: {data_barang[nama_barang]['stok']}")

def menu():
    print("\nMenu:")
    print("1. Input Data Barang")
    print("2. Tampil Data Barang")
    print("3. Hapus Data Barang")
    print("4. Cari Data Barang")
    print("5. Hitung Pembelian")
    print("6. Keluar")

def main():
    while True:
        menu()
        pilihan = input("Pilih menu (1-6): ")
        if pilihan == '1':
            input_barang()
        elif pilihan == '2':
            tampil_barang()
        elif pilihan == '3':
            hapus_barang()
        elif pilihan == '4':
            cari_barang()
        elif pilihan == '5':
            hitung_pembelian()
        elif pilihan == '6':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")

if __name__ == "__main__":
    main()
