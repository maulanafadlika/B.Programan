import os

daftar_buku = []

def pause():
    input("Tekan Enter untuk melanjutkan...")

def clear_output():
  if os.name == 'nt':
      os.system('cls')
  else:
    os.system('clear')

def tambah_buku():
  clear_output()
  judul = input("Masukkan judul buku: ")
  penulis = input("Masukkan penulis buku: ")
  while True:
    try:
      tahun = int(input("Masukkan tahun rilis: "))
      break
    except ValueError:
      print("Tahun rilis harus berupa angka. Silakan coba lagi.")
  daftar_buku.append({"judul": judul, "penulis": penulis, "tahun": tahun})
  clear_output()
  print("Buku berhasil ditambahkan!")
  pause()

def tampilkan_buku():
  clear_output()
  if not daftar_buku:
    print("Belum ada buku yang ditambahkan.")
  else:
    print("Daftar Buku:")
    for buku in daftar_buku:
      print("- Judul:", buku["judul"])
      print("  Penulis:", buku["penulis"])
      print("  Tahun Rilis:", buku["tahun"])
  pause()

def cari_buku():
  while True:
    clear_output()
    print("Silakan pilih metode pencarian:")
    print("1. Cari berdasarkan judul")
    print("2. Cari berdasarkan tahun rilis")
    print("3. Cari berdasarkan penulis")
    print("4. Kembali ke menu utama")

    pilihan = input("Masukkan pilihan Anda (1/2/3/4): ")

    if pilihan == "1":
      judul_cari = input("Masukkan judul buku: ")
      hasil = [buku for buku in daftar_buku if judul_cari.lower() in buku["judul"].lower()]
    elif pilihan == "2":
      while True:
        try:
          tahun_cari = int(input("Masukkan tahun rilis: "))
          break
        except ValueError:
          print("Tahun rilis harus berupa angka. Silakan coba lagi.")
      hasil = [buku for buku in daftar_buku if buku["tahun"] == tahun_cari]
    elif pilihan == "3":
      penulis_cari = input("Masukkan nama penulis: ")
      hasil = [buku for buku in daftar_buku if penulis_cari.lower() in buku["penulis"].lower()]
    elif pilihan == "4":
      return
    else:
      print("Pilihan tidak valid.")
      continue

    if hasil:
      print("\nHasil pencarian:")
      for buku in hasil:
        print("- Judul:", buku["judul"])
        print("  Penulis:", buku["penulis"])
        print("  Tahun Rilis:", buku["tahun"])
    else:
      print("Buku tidak ditemukan.")
    pause()

while True:
  clear_output()
  print("Selamat datang di Gramedia Berkah!")
  print("Menu:")
  print("1. Tambah Buku")
  print("2. Tampilkan Semua Buku")
  print("3. Cari Buku")
  print("4. Keluar")

  pilihan = input("Masukkan pilihan Anda (1/2/3/4): ")

  if pilihan == "1":
    tambah_buku()
  elif pilihan == "2":
    tampilkan_buku()
  elif pilihan == "3":
    cari_buku()
  elif pilihan == "4":
    clear_output()
    print("Terima kasih telah menggunakan Gramedia Berkah!")
    break
  else:
    print("Pilihan tidak valid.")
    pause()
