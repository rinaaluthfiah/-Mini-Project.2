from prettytable import PrettyTable

# Membuat tabel produk
tabel = PrettyTable()
tabel.field_names = ["No Produk", "Nama Produk", "Ukuran Produk", "Harga"]

# Fungsi untuk menambahkan produk air galon ke daftar yang tersedia
def tambah_produk(no_produk, nama_produk, ukuran_produk, harga):
    tabel.add_row([no_produk, nama_produk, ukuran_produk, harga])

# Data produk air galon yang tersedia
tambah_produk("1", "Air Galon Le Minerale", "15 Liter", 22900)
tambah_produk("2", "Air Galon Cleo", "12 Liter", 18900)
tambah_produk("3", "Air Galon Aqua", "19 Liter", 23500)
tambah_produk("4", "Air Galon Pristine", "19 Liter", 15000)
tambah_produk("5", "Air Galon Crystaline", "19 Liter", 17800)
tambah_produk("6", "Air Galon Tulus", "16 Liter", 20000)

# Membuat fungsi untuk login 
def login():
    while True:
        print('================== 🍶 SELAMAT DATANG DI DEPO AIR MINUM INOY 🍶==================')
        print("Segarkan Harimu dengan Air Putih yang sehat")
        print("[1.] Mimin")            # login sebagai penjual (mimin)
        print("[2.] Pembeli")          # login sebagai pembeli
        pilihan = input("Silahkan pilih untuk login : ") 
        if pilihan == "1":
            login_admin()
            Mimin()
        elif pilihan == "2":
            Pembeli()
            break
        else:
            print("Sesi Login Tidak ada, cobalah kembali!")
            return login()

# Akses Admin Untuk login
def login_admin():
    print("---------------Halo, Silahkan Login Mimin!----------------")
    while True:
        username = input("Masukkan Username anda: ")
        password = int(input("Masukkan Password anda: "))
        if username == 'Lily' and password == 234:
            print("Login berhasil!")
            Mimin()
            break
        else:
            print("Username atau Password salah. Coba lagi.")

# Fungsi Mimin (Admin)
def Mimin():
    while True:
        print("=================Selamat Datang Mimin Tercinta!==============")
        print("[1]. Tambah Produk")
        print("[2]. Lihat Produk")
        print("[3]. Hapus Produk")
        print("[4]. Perbarui Produk")
        print("[5]. Keluar")
        fitur = input("Silahkan pilih fitur: ")
        if fitur == "1":
            tambah_produk_mimin()
        elif fitur == "2":
            lihat_produk()
        elif fitur == "3":
            hapus_produk()
        elif fitur == "4":
            perbarui_produk()
        elif fitur == "5":
            login = input("Apa anda ingin keluar? (y/n) : ")
            if login == "n":
                print("Terimakasih Telah Menggunakan Program ini sahabat")
            break
        else:
            print("Pilihan salah")

# Fitur tambah produk untuk mimin
def tambah_produk_mimin():
    lihat_produk() # Menampilkan produk yang ada
    while True:
        no_produk = input("Masukan no produk : ")
        nama_produk = input("Masukan nama produk : ")
        ukuran_produk = input("Masukkan ukuran produk: ")
        harga = int(input("Masukan Harga produk: "))  # Memastikan harga dalam bentuk angka
        tambah_produk(no_produk, nama_produk, ukuran_produk, harga)
        pilihan = input("Ingin tambah barang lagi? (y/n) : ").lower()
        if pilihan != "y":  # Jika bukan 'y' keluar dari loop 
            break

# Fitur lihat produk untuk mimin
def lihat_produk():
    print(tabel)

# Fitur hapus produk untuk mimin 
def hapus_produk():
    lihat_produk()
    no_produk = input("Masukkan no produk yang ingin dihapus: ")
    produk_hapus = False
    for row in tabel._rows:
        if row[0] == no_produk:
            tabel._rows.remove(row)
            print(f'Produk dengan nomor [{no_produk}] telah dihapus')
            produk_hapus = True
            break
    if not produk_hapus:
        print(f'Produk dengan nomor [{no_produk}] tidak ditemukan')

# Fitur perbarui produk untuk mimin 
def perbarui_produk():
    lihat_produk()
    no_produk = input("Masukkan nomor produk yang ingin diperbarui: ")
    produk = False
    for row in tabel._rows:
        if row[0] == no_produk:
            produk = True
            break
    if not produk:
        print(f'Produk dengan nomor [{no_produk}] tidak ditemukan')
        return
    nama_produk = input("Masukan nama produk: ")
    ukuran_produk = input("Masukkan ukuran produk: ")
    harga_produk = input("Masukan Harga Produk: ")
    
    for row in tabel._rows:
        if row[0] == no_produk:
            if nama_produk:
                row[1] = nama_produk
            if ukuran_produk:
                row[2] = ukuran_produk
            if harga_produk:
                row[3] = int(harga_produk)  # Pastikan harga dalam bentuk angka
            print(f'Produk dengan nomor [{no_produk}] telah diperbarui')
            return

# Akses Login untuk Pembeli 
def Pembeli():
    print(">>>>>>>>>>>>>>Selamat Datang Pembeli tercinta!>>>>>>>>>>>>>>>>")
    nama_pembeli = input("Sebutkan Nama Anda : ")
    lihat_produk()
    print(f"Halo, {nama_pembeli}! Produk galon seperti apa yang ingin Anda beli?")
    
    no_produk = input("Masukkan Nomor Produk yang ingin dibeli: ") 
    for row in tabel._rows:
        if row[0] == no_produk:  #  melakukan cek apakah nomor barang cocok
            jumlah_produk = int(input("Masukkan jumlah produk yang ingin dibeli: "))
            harga = row[3]  # Harganya sudah dalam bentuk angka
            total_harga = jumlah_produk * harga  # Menghitung total harga keseluruhan
            print(f"Anda membeli {jumlah_produk} {row[1]} seharga Rp.{total_harga:,.0f}")  
            break
    else:
        print("Nomor Produk tidak valid. Silakan coba lagi.")  # Jika tidak ada barang yang cocok


login()