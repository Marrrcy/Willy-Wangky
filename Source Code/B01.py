# Josep Marcello / 16519170
# 8 April 2020
# Program encryption
# Program ini bisa membuat key, meload key, mengenkripsi, dan mendekripsi file

# TODO
# Definisi fungsi dan prosedur

# KAMUS
# hash, check_password : function

# ALGORTIMA 
# Menyiapkan library yang dibutuhkan
from hashlib import sha512
from uuid import uuid1

# PATH_TO_DB adalah sebuah variabel konstan untuk pathing ke direktori/folder Database
PATH_TO_DB = "../Database/"

# Realisasi fungsi dan prosedur
def hash(Password):
    # KAMUS LOKAL
	# salt : hex untuk random number

    # ALGORITMA FUNGSI
	# Membuat salt (pengaman password) dengan random number generator
    salt = uuid1().hex
	# Menyimpan salt dengan password
    Password = sha512(Password.encode()+salt.encode()).hexdigest() + ":" + salt
    return Password

def check_password(PasswordInput,PasswordUser):
	# KAMUS LOKAL
	# Salt : hex untuk random number
	
	# ALGORITMA FUNGSI
	# Memisahkan password yang sudah ditambahkan salt dengan salt-nya
    PasswordUser,Salt = PasswordUser.split(":")
	# Mencocokan password yang sudah ditambahkan salt dengan password yang diinput kemudian ditambah salt
    return PasswordUser == sha512(PasswordInput.encode()+Salt.encode()).hexdigest()

# Di bawah ini adalah kode untuk enkripsi file yang sudah tidak terpakai. Kenapa masih ada? Dibuang sayang!
# KAMUS
# UNUSED, dibuang sayang
# encrypt,decrypt,generate_key,create_key : prosedur
# load_key : function

# Loading library
# from cryptography.fernet import Fernet

# Realisasi fungsi dan prosedur
# def load_key():
#     # Membuka kunci untuk membuka enkripsi
#     return open("../Database/key.key", "rb").read()

# def encrypt(NamaFile, Key):
#     # KAMUS LOKAL
#     # f : kunci fernet
#     # encrypted_data : data file yang sudah dienkripsi
#     # file : file

#     # Algoritma prosedur
#     # Mengenkripsi file NamaFile dengan kunci Key
#     f = Fernet(Key)

#     # Membuka dan membaca file
#     with open(NamaFile, "rb") as file:
#         file_data = file.read()

#     # Mengenkripsi data
#     encrypted_data = f.encrypt(file_data)

#     # Membuka dan menuliskan file yang sudah dienkripsi
#     with open(NamaFile, "wb") as file:
#         file.write(encrypted_data)

# def decrypt(NamaFile, Key):
#     # KAMUS LOKAL
#     # f : kunci fernet
#     # decrypted_data : data file yang sudah dienkripsi
#     # file : file

#     # Mendekripsi file NamaFile dengan kunci Key
#     f = Fernet(Key)

#     # Membuka dan membaca file
#     with open(NamaFile, "rb") as file:
#         file_data = file.read()

#     # Mengenkripsi data
#     decrypted_data = f.decrypt(file_data)

#     # Membuka dan menuliskan file yang sudah dienkripsi
#     with open(NamaFile, "wb") as file:
#         file.write(decrypted_data)

# def create_key():
#     # KAMUS LOKAL
#     # key = Fernet key

#     # Membuat kunci enkripsi
#     key = Fernet.generate_key()
#     with open("../../Database/key.key", "wb") as key_file:
#         key_file.write(key)

# # ALGORITMA UTAMA
# if (__name__ == "__main__"):
#     key = load_key()
#     FileUser = PATH_TO_DB+"user.csv"
#     Filewahana = PATH_TO_DB+"wahana.csv"
#     Filepembelian = PATH_TO_DB+"pembelian.csv"
#     Filepenggunaan = PATH_TO_DB+"penggunaan.csv"
#     FileUtiket= PATH_TO_DB+"tiket.csv"
#     Filrefund = PATH_TO_DB+"refund.csv"
#     Filekritiksaran = PATH_TO_DB+"kritiksaran.csv"
#     FileUstikethilang =  PATH_TO_DB+"tikethilang.csv"

#     while True:
#         Masukkan = input("d = dekripsi\ne = enkripsi\ng = generate key\nlainnya = exit\n$ ")
#         Masukkan = Masukkan.lower()
#         if (Masukkan == 'd'):
#             decrypt(FileUser, key)
#             decrypt(Filewahana, key)
#             decrypt(Filepembelian, key)
#             decrypt(Filepenggunaan, key)
#             decrypt(FileUtiket, key)
#             decrypt(Filrefund, key)
#             decrypt(Filekritiksaran, key)
#             decrypt(FileUstikethilang, key)

#             print("Files have been decrypted")
#         elif (Masukkan == 'e'):
#             encrypt(FileUser, key)
#             encrypt(Filewahana, key)
#             encrypt(Filepembelian, key)
#             encrypt(Filepenggunaan, key)
#             encrypt(FileUtiket, key)
#             encrypt(Filrefund, key)
#             encrypt(Filekritiksaran, key)
#             encrypt(FileUstikethilang, key)

#             print("Files have been encrypted")
#         elif (Masukkan == 'g'):
#             check = False
#             check = input("Apakah anda yakin (y/n)?\nPastikan file sudah didekripsi semua dan sudah dibackup!\n$ ")
#             check = check.lower()
#             if (check == 'y'):
#                 create_key()
#                 key = load_key()
#         else:
#             break