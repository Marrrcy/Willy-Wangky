# Josep Marcello
# 8 April 2020
# Program SignUp
# Untuk menambahkan user ke program WillyWangky

# TODO
# Definisi fungsi dan prosedur

# KAMUS
# signup : function

# ALGORITMA UTAMA
# Loading library
import B01

# Definisi prosedur dan fungsi
def signup(User,DictionaryPassword):
    # KAMUS LOKAL
    # Nama, TanggalLahir, TinggiBadan, Username, Password : String
    # InfoUser : dictionary of strings

    # ALGORITMA FUNGSI
    # Inisialisasi dictionary
    InfoUser = {}

    # Menerima informasi pengguna
    Nama = input("Masukkan nama pemain: ")
    TanggalLahir = input("Masukkan tanggal lahir pemain (DD/MM/YYYY): ")
    TinggiBadan = input("Masukkan tinggi badan pemain (dalam cm): ")
    Username = input("Masukkan username pemain: ")
    # Memeriksa username sudah digunakan atau belum
    while(Username in DictionaryPassword):
        # Jika username sudah digunakan
        print("Username yang anda masukkan sudah terdaftarkan. Silakan pilih username lain.")
        Username = input("Masukkan username pemain: ")
    Password = input("Masukkan password pemain: ")
    Password = B01.hash(Password)

    # Menambahkan pasangan key dan value (username dan password) baru
    DictionaryPassword[Username] = Password

    # Menambahkan key dan value ke InfoUser (data pengguna)
    InfoUser["Nama"] = Nama
    InfoUser["TanggalLahir"] = TanggalLahir
    InfoUser["TinggiBadan"] = TinggiBadan
    InfoUser["Username"] = Username
    InfoUser["Password"] = Password
    InfoUser["Role"] = "Pemain"
    InfoUser["Saldo"] = "50000"
    InfoUser["StatusGold"] = "False"
    
    # Menambahkan data pengguna baru ke database
    User.append(InfoUser)

    # Pesan konfirmasi pengguna sudah berhasil didaftarkan
    print("Pengguna baru sudah didaftarkan! Selamat datang {} dan selamat bermain!".format(Nama))
    return User,DictionaryPassword,InfoUser