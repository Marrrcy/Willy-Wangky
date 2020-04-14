# Josep Marcello / 16519170
# 7 April 2020
# Program save
# Program ini akan menyimpan perubahan-perubahan yang dilakukan ke file CSV

# TODO

# KAMUS

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
def save(User,Wahana,Pembelian,Penggunaan,Tiket,Refund,KritikSaran,TiketHilang):
    # Membuka file-file CSV lalu memasukkannya ke dalam suatu variabel
    # KAMUS LOKAL
    # FileUser : SEQFILE of :
    #   (*) : csvUser : array[0..7] of string
    #   (1) : CONST_VARS.MARK_8

    # FileWahana : SEQFILE of :
    #   (*) : csvWahana : array[0..4] of string
    #   (1) : CONST_VARS.MARK_5

    # FilePembelian : SEQFILE of :
    #   (*) : csvPembelian : array[0..3] of string
    #   (1) : CONST_VARS.MARK_4
    
    # FilePenggunaan : SEQFILE of :
    #   (*) : csvPenggunaan : array[0..3] of string
    #   (1) : CONST_VARS.MARK_4

    # FileTiket : SEQFILE of :
    #   (*) : csvTiket : array[0..2] of string
    #   (1) : CONST_VARS.MARK_3

    # FileRefund : SEQFILE of :
    #   (*) : csvRefund : array[0..3] of string
    #   (1) : CONST_VARS.MARK_4

    # FileKritikSaran : SEQFILE of :
    #   (*) : csvKritikSaran : array[0..3] of string
    #   (1) : CONST_VARS.MARK_4

    # FileTiketHilang : SEQFILE of :
    #   (*) : csvTiketHilang : array[0..3] of string
    #   (1) : CONST_VARS.MARK_4

    # csvWriter_User : array[1..CONST_VARS.N] of array[1..8] of strings
    # csvWriter_Wahana : array[1..CONST_VARS.N] of array[1..5] of strings
    # csvWriter_Pembelian : array[1..CONST_VARS.N] of array[1..4] of strings
    # csvWriter_Penggunaan : array[1..CONST_VARS.N] of array[1..4] of strings
    # csvWriter_Tiket :array[1..CONST_VARS.N] of array[1..3] of strings
    # csvWriter_Refund : array[1..CONST_VARS.N] of array[1..4] of strings
    # csvWriter_KritikSaran : array[1..CONST_VARS.N] of array[1..4] of strings
    # csvWriter_TiketHilang : array[1..CONST_VARS.N] of array[1..4] of strings

    # ALGORITMA fungsi

    # Menerima nama file
    FileUser = input("Masukkan nama File User (default: user): ")
    # Menambahkan path ke file csv
    FileUser = CONST_VARS.PATH_TO_DB + FileUser
    
    FileWahana = input("Masukkan nama File Daftar Wahana (default: wahana): ")
    FileWahana = CONST_VARS.PATH_TO_DB + FileWahana

    FilePembelian = input("Masukkan nama File Pembelian Tiket (default: pembelian): ")
    FilePembelian = CONST_VARS.PATH_TO_DB + FilePembelian

    FilePenggunaan = input("Masukkan nama File Penggunaan Tiket (default: penggunaan): ")
    FilePenggunaan = CONST_VARS.PATH_TO_DB + FilePenggunaan

    FileTiket = input("Masukkan nama File Kepemilikan Tiket (default: tiket): ")
    FileTiket = CONST_VARS.PATH_TO_DB + FileTiket

    FileRefund = input("Masukkan nama File Refund Tiket (default: refund): ")
    FileRefund = CONST_VARS.PATH_TO_DB + FileRefund

    FileKritikSaran = input("Masukkan nama File Kritik dan Saran (default: kritiksaran): ")
    FileKritikSaran = CONST_VARS.PATH_TO_DB + FileKritikSaran

    FileTiketHilang = input("Masukkan nama File Kehilangan Tiket (default: tikethilang): ")
    FileTiketHilang = CONST_VARS.PATH_TO_DB + FileTiketHilang
    
    # Mengassign ke variabel
    # Databaser User
    csvUser = open(FileUser, 'w', newline = '') # Membuka file
    csvWriter_User = csv.writer(csvUser) # Membaca file secara csv

    # Memasukkan elemen per elemen dari database ke file dengan 1 baris per elemen
    for row in (User):
        csvWriter_User.writerow(row)

    # Ketika file sudah habis

    csvUser.close() # Menutup file

    # Database Wahana
    csvWahana = open(FileWahana, 'w') # Membuka file
    csvWriter_Wahana = csv.writer(csvWahana) # Membaca file secara csv

    # Memasukkan elemen per elemen dari database ke file dengan 1 baris per elemen
    for row in (Wahana):
        csvWriter_Wahana.writerow(row)

    # Ketika file sudah habis

    csvWahana.close() # Menutup file

    # Database Pembelian
    csvPembelian = open(FilePembelian, 'w') # Membuka file
    csvWriter_Pembelian = csv.writer(csvPembelian) # Membaca file secara csv

    # Memasukkan elemen per elemen dari database ke file dengan 1 baris per elemen
    for row in (Pembelian):
        csvWriter_Pembelian.writerow(row)

    # Ketika file sudah habis

    csvPembelian.close() # Menutup file
    
    # Database Penggunaan
    csvPenggunaan = open(FilePenggunaan, 'w') # Membuka file
    csvWriter_Penggunaan = csv.writer(csvPenggunaan) # Membaca file secara csv

    # Memasukkan elemen per elemen dari database ke file dengan 1 baris per elemen
    for row in (Penggunaan):
        csvWriter_Penggunaan.writerow(row)

    # Ketika file sudah habis

    csvPenggunaan.close() # Menutup file

    # Database Tiket
    csvTiket = open(FileTiket, 'w') # Membuka file
    csvWriter_Tiket = csv.writer(csvTiket) # Membaca file secara csv

    # Memasukkan elemen per elemen dari database ke file dengan 1 baris per elemen
    for row in (Tiket):
        csvWriter_Tiket.writerow(row)

    # Ketika file sudah habis

    csvTiket.close() # Menutup file

    # Database Refund
    csvRefund = open(FileRefund, 'w') # Membuka file
    csvWriter_Refund = csv.writer(csvRefund) # Membaca file secara csv

    # Memasukkan elemen per elemen dari database ke file dengan 1 baris per elemen
    for row in (Refund):
        csvWriter_Refund.writerow(row)

    # Ketika file sudah habis

    csvRefund.close() # Menutup file

    # Database KritikSaran
    csvKritikSaran = open(FileKritikSaran, 'w') # Membuka file
    csvWriter_KritikSaran = csv.writer(csvKritikSaran) # Membaca file secara csv

    # Memasukkan elemen per elemen dari database ke file dengan 1 baris per elemen
    for row in (KritikSaran):
        csvWriter_KritikSaran.writerow(row)

    # Ketika file sudah habis

    csvKritikSaran.close() # Menutup file

    # Database TiketHilang
    csvTiketHilang = open(FileTiketHilang, 'w') # Membuka file
    csvWriter_TiketHilang = csv.writer(csvTiketHilang) # Membaca file secara csv

    # Memasukkan elemen per elemen dari database ke file dengan 1 baris per elemen
    for row in (TiketHilang):
        csvWriter_TiketHilang.writerow(row)

    # Ketika file sudah habis

    csvTiketHilang.close() # Menutup file

    # Pesan konfirmasi file-file telah disave
    print("Semua file telah disimpan")