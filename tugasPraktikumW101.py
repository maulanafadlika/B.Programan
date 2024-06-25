import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print("Selamat datang di Program Pencarian")
    print("Pilih program pencarian yang ingin dijalankan:")
    print("1. Binary Search (Tema: Harga Barang)")
    print("2. Sequential Search (Tema: Nomor Telepon)")
    print("3. Binary Search (Contoh dari Gambar)")
    print("4. Keluar")

def binary_search_prices(items, price):
    low = 0
    high = len(items) - 1

    while low <= high:
        mid = (high + low) // 2
        if items[mid]['harga'] < price:
            low = mid + 1
        elif items[mid]['harga'] > price:
            high = mid - 1
        else:
            return mid
    return -1

def sequential_search(contacts, name):
    for i in range(len(contacts)):
        if contacts[i]['nama'] == name:
            return i
    return -1

def binary_search_example(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

def input_items():
    items = []
    n = int(input("Masukkan jumlah barang: "))
    for i in range(n):
        cls()
        nama = input(f"Masukkan nama barang ke-{i+1}: ")
        harga = int(input(f"Masukkan harga barang ke-{i+1}: "))
        items.append({'nama': nama, 'harga': harga})
        items.sort(key=lambda x: x['harga'])
        cls()
        print("Daftar barang yang sudah diinput:")
        for idx, item in enumerate(items):
            print(f"Barang ke-{idx+1}:")
            display_item(item)
            print()
    return items

def display_item(item):
    print(f"  Nama: {item['nama']}")
    print(f"  Harga: {item['harga']}")

def input_contacts():
    contacts = []
    n = int(input("Masukkan jumlah kontak: "))
    for i in range(n):
        cls()
        nama = input(f"Masukkan nama kontak ke-{i+1}: ")
        nomor = input(f"Masukkan nomor telepon ke-{i+1}: ")
        contacts.append({'nama': nama, 'nomor': nomor})
        cls()
        print("Daftar kontak yang sudah diinput:")
        for idx, contact in enumerate(contacts):
            print(f"Kontak ke-{idx+1}:")
            display_contact(contact)
            print()
    return contacts

def display_contact(contact):
    print(f"  Nama: {contact['nama']}")
    print(f"  Nomor Telepon: {contact['nomor']}")

def main():
    while True:
        cls()
        menu()
        choice = input("Masukkan pilihan Anda: ")

        if choice == '1':
            cls()
            items = input_items()
            price = int(input("Masukkan harga barang yang ingin dicari: "))
            result = binary_search_prices(items, price)
            if result != -1:
                print("Barang ditemukan:")
                display_item(items[result])
            else:
                print("Harga barang tidak ditemukan")
            input("\nTekan Enter untuk kembali ke menu...")

        elif choice == '2':
            cls()
            contacts = input_contacts()
            name = input("Masukkan nama kontak yang ingin dicari: ")
            result = sequential_search(contacts, name)
            if result != -1:
                print("Kontak ditemukan:")
                display_contact(contacts[result])
            else:
                print("Nama kontak tidak ditemukan")
            input("\nTekan Enter untuk kembali ke menu...")

        elif choice == '3':
            cls()
            arr = list(map(int, input("Masukkan daftar elemen yang sudah terurut (pisahkan dengan spasi): ").split()))
            x = int(input("Masukkan elemen yang akan dicari: "))
            result = binary_search_example(arr, x)
            if result != -1:
                print(f"Elemen ditemukan pada indeks {result}")
            else:
                print("Elemen tidak ditemukan dalam daftar")
            input("\nTekan Enter untuk kembali ke menu...")

        elif choice == '4':
            cls()
            print("Keluar dari program. Terima kasih!")
            break

        else:
            cls()
            print("Pilihan tidak valid. Silakan coba lagi.")
            input("\nTekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    main()
