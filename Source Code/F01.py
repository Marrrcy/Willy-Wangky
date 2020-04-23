# Josep Marcello / 16519170
# 7 April 2020
# Program load
# Program ini akan membaca dan menyiapkan file CSV

# TODO

# KAMUS

# definisi fungsi dan prosedur
# function load() --> array[0..CONST_VARS.N-1] of array[1..8] of strings,array[0..CONST_VARS.N-1] of array[1..5] of strings,
#                     array[0..CONST_VARS.N-1] of array[1..4] of strings,array[0..CONST_VARS.N-1] of array[1..4] of strings,
#                     array[0..CONST_VARS.N-1] of array[1..3] of strings,array[0..CONST_VARS.N-1] of array[1..4] of strings,
#                     array[0..CONST_VARS.N-1] of array[1..4] of strings,array[0..CONST_VARS.N-1] of array[1..4] of strings
# Fungsi akan me-load file-file csv lalu menyimpannya ke dalam array-array database

# ALGORTIMA utama
# Menyiapkan library yang dibutuhkan
import csv, CONST_VARS

# Realisasi fungsi dan prosedur
def load():
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

    # csvReader_User : array[1..CONST_VARS.N] of array[1..8] of strings
    # User : array[1..CONST_VARS.N] of array[1..8] of strings
    User = [[' ' for j in range(8)] for i in range(CONST_VARS.N)]

    # csvReader_Wahana : array[1..CONST_VARS.N] of array[1..5] of strings
    # Wahana : array[1..CONST_VARS.N] of array[1..5] of strings
    Wahana = [[' ' for i in range(5)] for j in range(CONST_VARS.N)]

    # csvReader_Pembelian : array[1..CONST_VARS.N] of array[1..4] of strings
    # Pembelian : array[1..CONST_VARS.N] of array[1..4] of strings
    Pembelian = [[' ' for i in range(4)] for j in range(CONST_VARS.N)]

    # csvReader_Penggunaan : array[1..CONST_VARS.N] of array[1..4] of strings
    # Penggunaan : array[1..CONST_VARS.N] of array[1..4] of strings
    Penggunaan = [[' ' for i in range(4)] for j in range(CONST_VARS.N)]

    # csvReader_Tiket :array[1..CONST_VARS.N] of array[1..3] of strings
    # Tiket :array[1..CONST_VARS.N] of array[1..3] of strings
    Tiket = [[' ' for i in range(3)] for j in range(CONST_VARS.N)]

    # csvReader_Refund : array[1..CONST_VARS.N] of array[1..4] of strings
    # Refund : array[1..CONST_VARS.N] of array[1..4] of strings
    Refund = [[' ' for i in range(4)] for j in range(CONST_VARS.N)]

    # csvReader_KritikSaran : array[1..CONST_VARS.N] of array[1..4] of strings
    # KritikSaran : array[1..CONST_VARS.N] of array[1..4] of strings
    KritikSaran = [[' ' for i in range(4)] for j in range(CONST_VARS.N)]

    # csvReader_TiketHilang : array[1..CONST_VARS.N] of array[1..4] of strings
    # TiketHilang : array[1..CONST_VARS.N] of array[1..4] of strings
    TiketHilang = [[' ' for i in range(4)] for j in range(CONST_VARS.N)]

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
    csvUser = open(FileUser, 'r') # Membuka file
    csvReader_User = csv.reader(csvUser) # Membaca file secara csv

    i = 0 # First element

    for row in (csvReader_User):
        User[i] = row # Memproses element
        i += 1 # Next element

    # Ketika file sudah habis

    csvUser.close() # Menutup file

    # Database Wahana
    csvWahana = open(FileWahana, 'r') # Membuka file
    csvReader_Wahana = csv.reader(csvWahana) # Membaca file secara csv

    i = 0 # First element

    for row in (csvReader_Wahana):
        Wahana[i] = row # Memproses element
        i += 1 # Next element

    # Ketika file sudah habis

    csvWahana.close() # Menutup file

    # Database Pembelian
    csvPembelian = open(FilePembelian, 'r') # Membuka file
    csvReader_Pembelian = csv.reader(csvPembelian) # Membaca file secara csv

    i = 0 # First element

    for row in (csvReader_Pembelian):
        Pembelian[i] = row # Memproses element
        i += 1 # Next element

    # Ketika file sudah habis

    csvPembelian.close() # Menutup file
    
    # Database Penggunaan
    csvPenggunaan = open(FilePenggunaan, 'r') # Membuka file
    csvReader_Penggunaan = csv.reader(csvPenggunaan) # Membaca file secara csv

    i = 0 # First element

    for row in (csvReader_Penggunaan):
        Penggunaan[i] = row # Memproses element
        i += 1 # Next element

    # Ketika file sudah habis

    csvPenggunaan.close() # Menutup file

    # Database Tiket
    csvTiket = open(FileTiket, 'r') # Membuka file
    csvReader_Tiket = csv.reader(csvTiket) # Membaca file secara csv

    i = 0 # First element

    for row in (csvReader_Tiket):
        Tiket[i] = row # Memproses element
        i += 1 # Next element

    # Ketika file sudah habis

    csvTiket.close() # Menutup file

    # Database Refund
    csvRefund = open(FileRefund, 'r') # Membuka file
    csvReader_Refund = csv.reader(csvRefund) # Membaca file secara csv

    i = 0 # First element

    for row in (csvReader_Refund):
        Refund[i] = row # Memproses element
        i += 1 # Next element

    # Ketika file sudah habis

    csvRefund.close() # Menutup file

    # Database KritikSaran
    csvKritikSaran = open(FileKritikSaran, 'r') # Membuka file
    csvReader_KritikSaran = csv.reader(csvKritikSaran) # Membaca file secara csv

    i = 0 # First element

    for row in (csvReader_KritikSaran):
        KritikSaran[i] = row # Memproses element
        i += 1 # Next element

    # Ketika file sudah habis

    csvKritikSaran.close() # Menutup file

    # Database TiketHilang
    csvTiketHilang = open(FileTiketHilang, 'r') # Membuka file
    csvReader_TiketHilang = csv.reader(csvTiketHilang) # Membaca file secara csv

    i = 0 # First element

    for row in (csvReader_TiketHilang):
        TiketHilang[i] = row # Memproses element
        i += 1 # Next element

    # Ketika file sudah habis

    csvTiketHilang.close() # Menutup file

    # Pesan konfirmasi file-file telah diload
    print("Semua file telah diload.")
    
    return User,Wahana,Pembelian,Penggunaan,Tiket,Refund,KritikSaran,TiketHilang