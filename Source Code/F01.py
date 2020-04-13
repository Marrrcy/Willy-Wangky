# Josep Marcello / 16519170
# 7 April 2020
# Program load
# Program ini akan membaca dan menyiapkan file CSV

# TODO
# Definisi fungsi dan prosedur

# KAMUS
# PATH_TO_DB: string
# load_key, load : fungsi

# ALGORTIMA utama
# Menyiapkan library yang dibutuhkan
import csv

# PATH_TO_DB adalah sebuah variabel konstan untuk pathing ke direktori/folder Database
PATH_TO_DB = "../Database/"

# Realisasi fungsi dan prosedur
def load_csv(NamaFile):
    # KAMUS LOKAL
    # CsvReader, TempReader : array of string dictionary
    # CsvFile : file Csv
    # NamaFile : string
    # key : key for decrypting purposes

    # ALGORITMA Fungsi
    # Inisialisai variabel
    TempReader = []
    # mengubah nama file yang diinput menjadi huruf kecil semua
    NamaFile = NamaFile.lower() 
    # menambahkan pathing ke folder database
    NamaFile = PATH_TO_DB + NamaFile 

    # Menambahkan tipe file jika lupa ditambahkan saat input
    if not((".csv") in NamaFile): 
        NamaFile += ".csv"

    # Mengoperasikan file
    with open(NamaFile, 'r') as CsvFile:
        # Membaca (parsing) file csv sebagai dictionary
        CsvReader = csv.DictReader(CsvFile) 
        
        for lines in CsvReader:
            # Menyimpan file csv tadi ke TempReader, baris per baris
            TempReader.append(lines) 

    # mengembalikan dictionary
    return TempReader 

def load():
    # KAMUS LOKAL
    # FileKritikSaran, FilePembelian, FilePenggunaan, FilePenggunaan, FileRefund, FileTiket, FileTiketHilang, FileUser, FileWahana : string 
    # User, Wahana, Pembelian, Penggunaan, Tiket, Refund, KritikSaran, TiketHilang : array of string dictionary
    # DictionaryPassword : dictionary of string

    # ALGORITMA fungsi
    # Inisialisasi dictionary
    DictionaryPassword = {}
    # Menerima nama file
    FileUser = input("Masukkan nama File User (default: user): ")
    FileWahana = input("Masukkan nama File Daftar Wahana (default: wahana): ")
    FilePembelian = input("Masukkan nama File Pembelian Tiket (default: pembelian): ")
    FilePenggunaan = input("Masukkan nama File Penggunaan Tiket (default: penggunaan): ")
    FileTiket = input("Masukkan nama File Kepemilikan Tiket (default: tiket): ")
    FileRefund = input("Masukkan nama File Refund Tiket (default: refund): ")
    FileKritikSaran = input("Masukkan nama File Kritik dan Saran (default: kritiksaran): ")
    FileTiketHilang = input("Masukkan nama File Kehilangan Tiket (default: tikethilang): ")
    
    # Membuka file lalu diassign ke variabel
    User = load_csv(FileUser)
    Wahana = load_csv(FileWahana)
    Pembelian = load_csv(FilePembelian)
    Penggunaan = load_csv(FilePenggunaan)
    Tiket = load_csv(FileTiket)
    Refund = load_csv(FileRefund)
    KritikSaran = load_csv(FileKritikSaran)
    TiketHilang = load_csv(FileTiketHilang)

    # Menambahkan username dan password ke dictionary dengan username sebagai value
    for user_ite in User:
        DictionaryPassword[user_ite['Username']] = user_ite['Password']

    # Pesan konfirmasi file-file telah diload
    print("Semua file telah diload")
    # Mengembalikan dictionary dari file ke program utama
    return User,Wahana,Pembelian,Penggunaan,Tiket,Refund,KritikSaran,TiketHilang,DictionaryPassword