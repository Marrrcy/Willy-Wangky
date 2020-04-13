# Josep Marcello / 16519170
# 8 April 2020
# Program WillyWangky
# Main program dan interface dengan pengguna

# TODO
# Komentar
# Ganti nama variabel yang nampung file csv yg udh dibuka
# Aksi == cari, lihat_laporan, beli_tiket, main, refund, kritik_saran

# KAMUS
# Aksi : string
# DatabaseUser,Wahana,Pembelian,Penggunaan,Tiket,Refund,KritikSaran,TiketHilang : array of string dictionary
# DictionaryPassword, InfoUser : dictionary of string
# Loaded, Login, Sudo : boolean
# YesNo : character

# ALGORITMA
# load library
import F01,F02,F03,F04,F05,F06,F12

# # function panjangArray (arr : integer) --> integer
# def panjangArray(arr):
#     # KAMUS LOKAL
#     # count : integer

#     # ALGORITMA FUNGSI
#     # Inisialisasi variabel
#     count = 0

#     # Meloop setiap elemen dalam arr untuk menghitung jumlah elemennya
#     for i in arr:
#         count += 1

#     return count

# Inisialisasi variabel
# Menandakan belum loading jika false
Loaded = False
# Menandakan belum login jika false
LoggedIn = False
# Menandakan yang mengakses adalah pemain jika false
Sudo = False

# Agar program terus berjalan
while (True):

    # Menerima input apa yang mau dilakukan user
    Aksi = input("Apa yang mau kamu lakukan?\n$ ")

    # Mengubah input menjadi huruf kecil
    Aksi = Aksi.lower()
    # me-load file
    if (Aksi == "load"):
        DatabaseUser,DatabaseWahana,DatabasePembelian,DatabasePenggunaan,DatabaseTiket,DatabaseRefund,DatabaseKritikSaran,DatabaseTiketHilang = F01.load()
        # Menandakan sudah loading
        Loaded = True
    # exit/menghentikan program
    elif (Aksi == "exit"):
        # Jika file sudah diload sebelumnya
        if (Loaded):
            YesNo = input("Apakah anda mau menyimpan file (y/n)? ")

            if (YesNo == 'y'):
                F02.save(DatabaseUser,DatabaseWahana,DatabasePembelian,DatabasePenggunaan,DatabaseTiket,DatabaseRefund,DatabaseKritikSaran,DatabaseTiketHilang)
        break

    # Menyimpan, login, atau mencari wahana
    elif (Aksi == "login" or Aksi == "save" or Aksi == "cari"):
        if not(Loaded):
            print("Load file yang dibutuhkan terlebih dahulu dengan perintah 'load' (tanpa kutip)!")
        else:
            if (Aksi == "login"):
                LoggedIn, IndexUser = F04.login(DatabaseUser)
                InfoUser = DatabaseUser[IndexUser]
                # Memeriksa apakah admin yang login atau bukan
                # Yang login adalah admin
                if (InfoUser["Role"] == "admin"): 
                    Sudo = True
                else: # Yang login adalah pemain
                    Sudo = False
            # save/menyimpan
            elif (Aksi == "save"):
                F02.save(DatabaseUser,DatabaseWahana,DatabasePembelian,DatabasePenggunaan,DatabaseTiket,DatabaseRefund,DatabaseKritikSaran,DatabaseTiketHilang)
            elif (Aksi == "cari"):
                F06.cari(DatabaseWahana)

    # Perintah-perintah yang hanya dapat diakses oleh admin
    # mendaftarkan pemain baru, pencarian pemain, melihat kritik dan saran, menambahkan wahana, topup saldo, atau melihat riwayat penggunaan wahana
    elif (Aksi == "signup" or Aksi == "cari_pemain" or Aksi == "lihat_laporan" or Aksi == "tambah_wahana" or Aksi == "topup" or Aksi == "riwayat_wahana"):
        # Jika file-file belum diload
        if not(Loaded):
            print("Load file yang dibutuhkan terlebih dahulu dengan perintah 'load' (tanpa kutip)!")
        # Jika yang mengakses adalah pemain
        if not(Sudo):
            print("Kamu tidak memiliki hak untuk mengakses command atau command tidak ada!")
        elif not(LoggedIn):
            print("Kamu belum login")
        # Jika yang mengakses adalah admin dan file sudah diload
        elif (Sudo and LoggedIn and Loaded):
            if (Aksi == "signup"):
                DatabaseUser, InfoUser = F03.signup(DatabaseUser)
            elif (Aksi == "cari_pemain"):
                F05.cari_pemain(DatabaseUser)
            elif (Aksi == "lihat_laporan"):
                None
            elif (Aksi == "tambah_wahana"):
                DatabaseWahana = F12.tambah_wahana(DatabaseWahana)
            elif (Aksi == "topup"):
                None
            elif (Aksi == "riwayat_wahana"):
                None

    # Perintah-perintah yang hanya dapat diakses oleh pemain
    elif (Aksi == "beli_tiket" or Aksi == "main" or Aksi == "refund" or Aksi == "kritik_saran"):
        # Jika file-file belum diload
        if not(Loaded):
            print("Load file yang dibutuhkan terlebih dahulu dengan perintah 'load' (tanpa kutip)!")
        # Jika yang mengakses adalah admin
        if Sudo:
            print("Kamu tidak memiliki hak untuk mengakses command atau command tidak ada!")
        elif not(LoggedIn):
            print("Kamu belum login")
        # Jika yang mengakses adalah pemain dan file sudah diload
        elif (not(Sudo) and LoggedIn and Loaded):
            if (Aksi == "beli_tiket"):
                None
            elif (Aksi == "main"):
                None
            elif (Aksi == "refund"):
                None
            elif (Aksi == "kritik_saran"):
                None
    # Jika command tidak ada
    else:
        print("Kamu tidak memiliki hak untuk mengakses command atau command tidak ada!")

print("Sedang keluar dari program...")
print("Sampai bertemu nanti!")