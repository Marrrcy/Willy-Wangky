# Josep Marcello / 16519170
# 8 April 2020
# Program WillyWangky
# Main program dan interface dengan pengguna

# TODO

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
import B02,B03,B04,F01,F02,F03,F04,F05,F06,F07,F08,F09,F10,F11,F12,F13,F14,F15,F16

# Inisialisasi variabel
# Menandakan belum loading jika false
Loaded = False
# Menandakan belum login jika false
LoggedIn = False
# Menandakan yang login adalah pemain jika false
Sudo = False
# Mengisi InfoUser
InfoUser = ["" for i in range(8)]

# Pesan untuk menyambut user
print("Selamat datang di")
print(" _    _ _ _ _         _    _                   _          ")
print("| |  | (_) | |       | |  | |                 | |         ")
print("| |  | |_| | |_   _  | |  | | __ _ _ __   __ _| | ___   _ ")
print("| |/\| | | | | | | | | |/\| |/ _` | '_ \ / _` | |/ / | | |")
print("\  /\  / | | | |_| | \  /\  / (_| | | | | (_| |   <| |_| |")
print(" \/  \/|_|_|_|\__, |  \/  \/ \__,_|_| |_|\__, |_|\_\ \_, |")
print("               __/ |                      __/ |      __/ |")
print("              |___/                      |___/      |___/ ")

# Login dan load pertama
print("Apa yang mau kamu lakukan?\n$ load")
# Meload file untuk pertama kali
DatabaseUser,DatabaseWahana,DatabasePembelian,DatabasePenggunaan,DatabaseTiket,DatabaseRefund,DatabaseKritikSaran,DatabaseTiketHilang = F01.load()

# Menandakan sudah loading
Loaded = True

# Login untuk pertama kali 
print("Apa yang mau kamu lakukan?\n$ login")
IndexUser = F02.login(DatabaseUser)
InfoUser = DatabaseUser[IndexUser]
LoggedIn = True

# Memeriksa apakah admin yang login atau bukan

if (InfoUser[5] == "admin"): # Yang login adalah admin
    Sudo = True
else: # Yang login adalah pemain
    Sudo = False

# Agar program terus berjalan
while (True):
    
    # Menerima input apa yang mau dilakukan user
    # Menu utama program
    Aksi = input("Apa yang mau kamu lakukan?\n$ ")

    # me-load file
    if (Aksi == "load"):
        DatabaseUser,DatabaseWahana,DatabasePembelian,DatabasePenggunaan,DatabaseTiket,DatabaseRefund,DatabaseKritikSaran,DatabaseTiketHilang = F01.load()
        # Menandakan sudah loading
        Loaded = True

    # exit/menghentikan program
    elif (Aksi == "exit"):
        print("Sampai bertemu di lain waktu {}!".format(InfoUser[0]))
        # Jika file sudah diload sebelumnya
        DatabaseUser[IndexUser] = InfoUser
        F16.exit(DatabaseUser,DatabaseWahana,DatabasePembelian,DatabasePenggunaan,DatabaseTiket,DatabaseRefund,DatabaseKritikSaran,DatabaseTiketHilang,Loaded)
        break

    # Menyimpan, login, atau mencari wahana
    elif (Aksi == "login" or Aksi == "save" or Aksi == "cari" or Aksi == "best_wahana"):
        if not(Loaded):
            print("Load file yang dibutuhkan terlebih dahulu dengan perintah 'load' (tanpa kutip)!")
        else: # File sudah diload
            if (Aksi == "login"):
                IndexUser = F02.login(DatabaseUser)
                InfoUser = DatabaseUser[IndexUser]
                LoggedIn = True

                # Memeriksa apakah admin yang login atau bukan
                if (InfoUser[5] == "admin"): # Yang login adalah admin
                    Sudo = True
                else: # Yang login adalah pemain
                    Sudo = False

            # save/menyimpan database
            elif (Aksi == "save"):
                DatabaseUser[IndexUser] = InfoUser
                F03.save(DatabaseUser,DatabaseWahana,DatabasePembelian,DatabasePenggunaan,DatabaseTiket,DatabaseRefund,DatabaseKritikSaran,DatabaseTiketHilang)
            
            # Mencari wahana
            elif (Aksi == "cari"):
                F06.cari(DatabaseWahana)
            
            # Melihat wahana terbaik
            elif (Aksi == "best_wahana"):
                B03.bestwahana(DatabasePembelian, DatabaseWahana)

    # Perintah-perintah yang hanya dapat diakses oleh admin
    # mendaftarkan pemain baru, pencarian pemelihat kritik dan saran, menambahkan wahana, topup saldo, atau melihat riwayat penggunaan wahana
    elif (Aksi == "signup" or Aksi == "cari_pemain" or Aksi == "lihat_laporan" or Aksi == "tambah_wahana" or Aksi == "topup" or Aksi == "riwayat_wahana" or Aksi == "tiket_pemain" or Aksi == "upgrade_gold"):

        if not(Loaded): # Jika file-file belum diload
            print("Load file yang dibutuhkan terlebih dahulu dengan perintah 'load' (tanpa kutip)!")
        elif not(Sudo): # Jika yang mengakses adalah pemain
            print("Kamu tidak memiliki hak untuk mengakses command atau command tidak ada!") 
        elif not(LoggedIn): # Jika belum login
            print("Kamu belum login")

        elif (Sudo and LoggedIn and Loaded): # Jika yang mengakses adalah admin dan file sudah diload
            # Mendaftarkan pemain baru
            if (Aksi == "signup"):
                DatabaseUser, IndexUser = F04.signup(DatabaseUser)
                InfoUser = DatabaseUser[IndexUser]

                 # Memeriksa apakah admin yang login atau bukan
                if (InfoUser[5] == "admin"): # Yang login adalah admin
                    Sudo = True
                else: # Yang login adalah pemain
                    Sudo = False           

            # Mencari pemain
            elif (Aksi == "cari_pemain"):
                F05.cari_pemain(DatabaseUser)
            
            # Melihat kritik dan saran
            elif (Aksi == "lihat_laporan"):
                F11.lihatkritikdansaran(DatabaseKritikSaran)

            # Menambahkan wahana baru
            elif (Aksi == "tambah_wahana"):
                DatabaseWahana = F12.tambah_wahana(DatabaseWahana)

            # Menambahkan saldo user (topup)
            elif (Aksi == "topup"):
                DatabaseUser = F13.topup(DatabaseUser)

            # Melihat riwayat penggunaan wahana
            elif (Aksi == "riwayat_wahana"):
                F14.lihatriwayatwahana(DatabasePenggunaan)

            # Melihat tiket yg dimiliki pemain
            elif (Aksi == "tiket_pemain"):
                F15.tiket_pemain(DatabaseTiket,DatabaseWahana)
                
            # Mengupgrade status gold pemain
            elif (Aksi == "upgrade_gold"):
                DatabaseUser = B02.up_gold(DatabaseUser)


    # Perintah-perintah yang hanya dapat diakses oleh pemain
    elif (Aksi == "beli_tiket" or Aksi == "main" or Aksi == "refund" or Aksi == "kritik_saran" or Aksi == "tiket_hilang"):

        if not(Loaded): # Jika file-file belum diload
            print("Load file yang dibutuhkan terlebih dahulu dengan perintah 'load' (tanpa kutip)!")
        elif Sudo: # Jika yang mengakses adalah admin
            print("Kamu tidak memiliki hak untuk mengakses command atau command tidak ada!")
        elif not(LoggedIn): # Jika belum login
            print("Kamu belum login")

        elif (not(Sudo) and LoggedIn and Loaded): # Jika yang mengakses adalah pemain dan file sudah diload
            # Membeli tiket
            if (Aksi == "beli_tiket"):
                InfoUser,DatabaseTiket,DatabasePembelian = F07.beli_tiket(InfoUser,DatabaseTiket,DatabasePembelian,DatabaseWahana)
            
            # Menggunakan tiket
            elif (Aksi == "main"):
                InfoUser,DatabaseTiket,DatabasePenggunaan,DatabaseWahana = F08.main(InfoUser,DatabaseTiket,DatabasePembelian,DatabaseWahana,DatabasePenggunaan)
            
            # Refund tiket
            elif (Aksi == "refund"):
                InfoUser, DatabaseTiket, DatabasePembelian, DatabaseRefund =  F09.refund(InfoUser,DatabaseTiket,DatabasePembelian,DatabaseWahana,DatabaseRefund) 
            
            # Memberikan kritik/saran
            elif (Aksi == "kritik_saran"):
                DatabaseKritikSaran = F10.KritikdanSaran(DatabaseKritikSaran, DatabaseWahana, InfoUser)
                
            # Melaporkan tiket hilang
            elif (Aksi == "tiket_hilang"):
                DatabaseTiketHilang,DatabaseTiket =  B04.tiket_hilang(DatabaseTiket, DatabaseTiketHilang)

    # Jika command tidak ada
    else:
        print("Kamu tidak memiliki hak untuk mengakses command atau command tidak ada!")
