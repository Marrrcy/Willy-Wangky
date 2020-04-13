# Josep Marcello / 16519170
# 7 April 2020
# Program save
# Program ini akan menyimpan perubahan-perubahan yang dilakukan ke file CSV

# TODO
# Definisi fungsi dan prosedur

# KAMUS
# PATH_TO_DB: string
# save_csv, save : prosedur

# ALGORTIMA utama
# Menyiapkan library yang dibutuhkan
import csv

# PATH_TO_DB adalah sebuah variabel konstan untuk pathing ke direktori/folder Database
PATH_TO_DB = "../Database/"

# Realisasi fungsi dan prosedur
def save_csv(NamaFile,NewDB):
    # KAMUS LOKAL
    # NamaFile : String
    # CsvFile : File CSV
    # fieldnames : array of string
    # CsvReader, CsvWriter : parsed csv file
    # key : key for encrypting purposes

    # ALGORITMA Prosedur
    # mengubah nama file yang diinput menjadi huruf kecil semua
    NamaFile = NamaFile.lower() 
    # menambahkan pathing ke folder database
    NamaFile = PATH_TO_DB + NamaFile 

    # Menambahkan tipe file jika lupa ditambahkan saat input
    if not((".csv") in NamaFile): 
        NamaFile += ".csv"

    # Bagian untuk mengambil header dari file csv (akan digunakan sebagai fieldnames)
    # Mengoperasikan file
    with open(NamaFile, 'r') as CsvFile:
        # Membaca (parsing) file
        CsvReader = csv.reader(CsvFile)

        # Menyimpan header ke fieldnames
        fieldnames = next(CsvReader)

    # Melakukan perubahan pada file
    with open (NamaFile, 'w') as CsvFile:
        # Membaca file csv sebagai dictionary dengan fieldnames 'fieldnames' dan delimiter tanda koma (',')
        CsvWriter = csv.DictWriter(CsvFile, fieldnames = fieldnames, delimiter = ',')
        # Menuliskan header
        CsvWriter.writeheader()
        
        # Menuliskan info baru (dan lama) ke file database-nya (file yang lama akan ditimpa)
        for line in NewDB:
            CsvWriter.writerow(line)

def save(User,Wahana,Pembelian,Penggunaan,Tiket,Refund,KritikSaran,TiketHilang):
    # print(__name__)
    # KAMUS LOKAL
    # FileKritikSaran, FilePembelian, FilePenggunaan, FilePenggunaan, FileRefund, FileTiket, FileTiketHilang, FileUser, FileWahana : string 
    # User, Wahana, Pembelian, Penggunaan, Tiket, Refund, KritikSaran, TiketHilang : array of string dictionary

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