# Josep Marcello / 16519170
# 7 April 2020
# Program save
# Program ini akan menyimpan perubahan-perubahan yang dilakukan ke file CSV

# TODO

# KAMUS
# PATH_TO_DB: string

# Definisi prosedur dan fungsi
''' procedure save(input User : array[1..CONST_VARS.N] of array[1..8] of strings
    input Wahana : array[1..CONST_VARS.N] of array[1..5] of strings
    input Pembelian : array[1..CONST_VARS.N] of array[1..4] of strings
    input Penggunaan : array[1..CONST_VARS.N] of array[1..4] of strings
    input Tiket :array[1..CONST_VARS.N] of array[1..3] of strings
    input Refund : array[1..CONST_VARS.N] of array[1..4] of strings
    input KritikSaran : array[1..CONST_VARS.N] of array[1..4] of strings
    input TiketHilang : array[1..CONST_VARS.N] of array[1..4] of strings,)'''
# procedure save(input NamaFile : string, input NewDB : array[1..CONST_VARS.N] of array[1..M] of strings)

# ALGORTIMA utama
# Menyiapkan library yang dibutuhkan
import csv, CONST_VARS

# Realisasi fungsi dan prosedur
# def save_csv(NamaFile,NewDB):
#     # I.S.: NamaFile dan NewDB Terdefinisi
#     # F.S.: NewDB tertuliskan ke NamaFile
#     # KAMUS LOKAL
#     # NamaFile : String

#     # NamaFile : SEQFILE of :
#     #   (*) : CsvFile : array[1..M] strings

#     # CsvWriter : array[1..N] of array[1..M] strings

#     # ALGORITMA Prosedur
#     # menambahkan path ke folder database
#     NamaFile = PATH_TO_DB + NamaFile 

#     # Menambahkan tipe file jika lupa ditambahkan saat input
#     if not((".csv") in NamaFile): 
#         NamaFile += ".csv"

#     # Melakukan perubahan pada file
#     with open (NamaFile, 'w') as CsvFile:
#         # Membaca file csv
#         CsvWriter = csv.writer(CsvFile)
        
#         # Menuliskan info baru (dan lama) ke file database-nya (file yang lama akan ditimpa)
#         for line in NewDB:
#             CsvWriter.writerow(line)

def save(User,Wahana,Pembelian,Penggunaan,Tiket,Refund,KritikSaran,TiketHilang):
    # I.S.: User, Wahana, Pembelian, Penggunaan, Tiket, Refund, KritikSaran, TiketHilang terdefinisi
    # F.S.: User, Wahana, Pembelian, Penggunaan, Tiket, Refund, KritikSaran, TiketHilang dituliskan ke file-file csv database
    # KAMUS LOKAL
    # FileKritikSaran, FilePembelian, FilePenggunaan, FilePenggunaan, FileRefund, FileTiket, FileTiketHilang, FileUser, FileWahana : string 

    # ALGORITMA Prosedur
    # Menerima nama file
    FileUser = input("Masukkan nama File User (default: user): ")
    FileWahana = input("Masukkan nama File Daftar Wahana (default: wahana): ")
    FilePembelian = input("Masukkan nama File Pembelian Tiket (default: pembelian): ")
    FilePenggunaan = input("Masukkan nama File Penggunaan Tiket (default: penggunaan): ")
    FileTiket = input("Masukkan nama File Kepemilikan Tiket (default: tiket): ")
    FileRefund = input("Masukkan nama File Refund Tiket (default: refund): ")
    FileKritikSaran = input("Masukkan nama File Kritik dan Saran (default: kritiksaran): ")
    FileTiketHilang = input("Masukkan nama File Kehilangan Tiket (default: tikethilang): ")

    # Proses penyimpanan file
    save_csv(FileUser,User)
    save_csv(FileWahana,Wahana)
    save_csv(FilePembelian,Pembelian)
    save_csv(FilePenggunaan,Penggunaan)
    save_csv(FileTiket,Tiket)
    save_csv(FileRefund,Refund)
    save_csv(FileKritikSaran,KritikSaran)
    save_csv(FileTiketHilang,TiketHilang)

    # Pesan konfirmasi file-file telah disimpan
    print("Semua file telah disave")