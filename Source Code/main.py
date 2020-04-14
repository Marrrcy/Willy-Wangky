# Josep Marcello / 16519170
# 8 April 2020
# Program WillyWangky
# Main program dan interface dengan pengguna

# TODO
# Komentar
# Aksi == cari, lihat_laporan, beli_tiket, main, refund, kritik_saran

# KAMUS

# Database User : array[1..CONST_VARS.N] of array[1..8] of strings
# DatabaseWahana : array[1..CONST_VARS.N] of array[1..5] of strings
# DatabasePembelian : array[1..CONST_VARS.N] of array[1..4] of strings
# DatabasePenggunaan : array[1..CONST_VARS.N] of array[1..4] of strings
# DatabaseTiket :array[1..CONST_VARS.N] of array[1..3] of strings
# DatabaseRefund : array[1..CONST_VARS.N] of array[1..4] of strings
# DatabaseKritikSaran : array[1..CONST_VARS.N] of array[1..4] of strings
# DatabaseTiketHilang : array[1..CONST_VARS.N] of array[1..4] of strings
# InfoUser : array[0..7] of string
# Loaded, Login, Sudo : boolean
# Aksi : string
# YesNo : character
# IndexUser : integer

# ALGORITMA
# load library
import CONST_VARS
import F01,F02,F03,F04,F05,F06,F12

# Inisialisasi variabel
# Menandakan belum loading jika false
Loaded = False
# Menandakan belum login jika false
LoggedIn = False
# Menandakan yang login adalah pemain jika false
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
                IndexUser = F04.login(DatabaseUser)
                InfoUser = DatabaseUser[IndexUser]
                LoggedIn = True

                # Memeriksa apakah admin yang login atau bukan
                if (InfoUser[5] == "admin"): # Yang login adalah admin
                    Sudo = True
                else: # Yang login adalah pemain
                    Sudo = False

            # save/menyimpan database
            elif (Aksi == "save"):
                F02.save(DatabaseUser,DatabaseWahana,DatabasePembelian,DatabasePenggunaan,DatabaseTiket,DatabaseRefund,DatabaseKritikSaran,DatabaseTiketHilang)
            
            # Mencari wahana
            elif (Aksi == "cari"):
                F06.cari(DatabaseWahana)

    # Perintah-perintah yang hanya dapat diakses oleh admin
    # mendaftarkan pemain baru, pencarian pemain, melihat kritik dan saran, menambahkan wahana, topup saldo, atau melihat riwayat penggunaan wahana
    elif (Aksi == "signup" or Aksi == "cari_pemain" or Aksi == "lihat_laporan" or Aksi == "tambah_wahana" or Aksi == "topup" or Aksi == "riwayat_wahana"):
        if not(Loaded): # Jika file-file belum diload
            print("Load file yang dibutuhkan terlebih dahulu dengan perintah 'load' (tanpa kutip)!")
        elif not(Sudo): # Jika yang mengakses adalah pemain
            print("Kamu tidak memiliki hak untuk mengakses command atau command tidak ada!") 
        elif not(LoggedIn): # Jika belum login
            print("Kamu belum login")
        elif (Sudo and LoggedIn and Loaded): # Jika yang mengakses adalah admin dan file sudah diload
            if (Aksi == "signup"):
                DatabaseUser, IndexUser = F03.signup(DatabaseUser)
                InfoUser = DatabaseUser[IndexUser]
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
        if not(Loaded): # Jika file-file belum diload
            print("Load file yang dibutuhkan terlebih dahulu dengan perintah 'load' (tanpa kutip)!")
        elif Sudo: # Jika yang mengakses adalah admin
            print("Kamu tidak memiliki hak untuk mengakses command atau command tidak ada!")
        elif not(LoggedIn): # Jika belum login
            print("Kamu belum login")
        elif (not(Sudo) and LoggedIn and Loaded): # Jika yang mengakses adalah pemain dan file sudah diload
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