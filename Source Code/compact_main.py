# Josep Marcello / 16519170
# 19 April 2020
# Program cp_main

# Spt program main sesesungguhnya, tapi dibuat untuk debugging

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
import csv
import B03,B04,F03,F04,F05,F06,F07,F10,F11,F12,F14,F15

# Inisialisasi variabel
# Menandakan belum loading jika false
Loaded = False
# Menandakan belum login jika false
LoggedIn = False
# Menandakan yang login adalah pemain jika false
Sudo = False
# Mengisi InfoUser
InfoUser = ["" for i in range(8)]

def load_csv(FileName):
    FileName = CONST_VARS.PATH_TO_DB+FileName

    with open(FileName, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        temp_db = list(csvreader)

    return temp_db

def load():
    return load_csv("user.csv"),load_csv("wahana.csv"),load_csv("pembelian.csv"),load_csv("penggunaan.csv"), load_csv("tiket.csv"), load_csv("refund.csv"), load_csv("kritiksaran.csv"),load_csv("tikethilang.csv")

def save(FileName,DB):
    FileName = CONST_VARS.PATH_TO_DB+FileName

    with open(FileName, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)

        csvwriter.writerows(DB)

Sudo = LoggedIn = False; Loaded = True

print("Loading file...")
DatabaseUser,DatabaseWahana,DatabasePembelian,DatabasePenggunaan,DatabaseTiket,DatabaseRefund,DatabaseKritikSaran,DatabaseTiketHilang = load()
print("File sudah diload.")

print("Silakan login")
IndexUser = F04.login(DatabaseUser)
InfoUser = DatabaseUser[IndexUser]
LoggedIn = True

if (InfoUser[5] == "admin"): # Yang login adalah admin
    Sudo = True
else: # Yang login adalah pemain
    Sudo = False

while (LoggedIn):
    Aksi = input("Apa yang mau kamu lakukan?\n$ ")
    # me-load file
    if (Aksi == "load"):
        print("Loading file...")
        DatabaseUser,DatabaseWahana,DatabasePembelian,DatabasePenggunaan,DatabaseTiket,DatabaseRefund,DatabaseKritikSaran,DatabaseTiketHilang = load()
        print("File sudah diload.")
    # exit/menghentikan program
    elif (Aksi == "exit"):
        # Jika file sudah diload sebelumnya
        if (Loaded):
            YesNo = input("Apakah anda mau menyimpan file (y/n)? ")

            if (YesNo == 'y'):
                print("Menyimpan file...")
                save("user.csv",DatabaseUser),save("wahana.csv",DatabaseWahana),save("pembelian.csv",DatabasePembelian),save("penggunaan.csv",DatabasePenggunaan), save("tiket.csv",DatabaseTiket), save("refund.csv",DatabaseRefund), save("kritiksaran.csv",DatabaseKritikSaran),save("tikethilang.csv",DatabaseTiketHilang)
                print("File tersimpan")
        break

    # Menyimpan, login, atau mencari wahana
    elif (Aksi == "login" or Aksi == "save" or Aksi == "cari" or Aksi == "best_wahana"):
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
                print("Menyimpan file...")
                save("user.csv",DatabaseUser),save("wahana.csv",DatabaseWahana),save("pembelian.csv",DatabasePembelian),save("penggunaan.csv",DatabasePenggunaan), save("tiket.csv",DatabaseTiket), save("refund.csv",DatabaseRefund), save("kritiksaran.csv",DatabaseKritikSaran),save("tikethilang.csv",DatabaseTiketHilang)
                print("File tersimpan")
            
            # Mencari wahana
            elif (Aksi == "cari"):
                F06.cari(DatabaseWahana)

            # Melihat wahana terbaik
            elif (Aksi == "best_wahana"):
                B03.bestwahana(DatabaseWahana)

    # Perintah-perintah yang hanya dapat diakses oleh admin
    # mendaftarkan pemain baru, pencarian pemain, melihat kritik dan saran, menambahkan wahana, topup saldo, atau melihat riwayat penggunaan wahana
    elif (Aksi == "signup" or Aksi == "cari_pemain" or Aksi == "lihat_laporan" or Aksi == "tambah_wahana" or Aksi == "topup" or Aksi == "riwayat_wahana" or Aksi == "tiket_pemain"):
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
                F14.lihatriwayatwahana(DatabaseWahana)
            elif (Aksi == "tiket_pemain"):
                F15.tiket_pemain(DatabaseTiket,DatabaseWahana)

    # Perintah-perintah yang hanya dapat diakses oleh pemain
    elif (Aksi == "beli_tiket" or Aksi == "main" or Aksi == "refund" or Aksi == "kritik_saran" or Aksi == "tiket_hilang"):
        if not(Loaded): # Jika file-file belum diload
            print("Load file yang dibutuhkan terlebih dahulu dengan perintah 'load' (tanpa kutip)!")
        elif Sudo: # Jika yang mengakses adalah admin
            print("Kamu tidak memiliki hak untuk mengakses command atau command tidak ada!")
        elif not(LoggedIn): # Jika belum login
            print("Kamu belum login")
        elif (not(Sudo) and LoggedIn and Loaded): # Jika yang mengakses adalah pemain dan file sudah diload
            if (Aksi == "beli_tiket"):
                DatabaseTiket,DatabasePembelian = F07.beli_tiket(InfoUser,DatabaseTiket,DatabasePembelian,DatabaseWahana)
            elif (Aksi == "main"):
                InfoUser,DatabaseTiket,DatabasePembelian,DatabaseWahana = F08.main(InfoUser,DatabaseTiket,DatabasePembelian,DatabaseWahana)
            elif (Aksi == "refund"):
                None
            elif (Aksi == "kritik_saran"):
                DatabaseKritikSaran = F10.KritikdanSaran(DatabaseKritikSaran, DatabaseWahana, InfoUser)
            elif (Aksi == "tiket_hilang"):
                DatabaseTiketHilang,DatabaseTiket =  B04.tiket_hilang(DatabaseTiket, DatabaseTiketHilang)
    # Jika command tidak ada
    else:
        print("Kamu tidak memiliki hak untuk mengakses command atau command tidak ada!")