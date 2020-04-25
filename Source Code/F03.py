# Josep Marcello
# 8 April 2020
# Program SignUp
# Untuk menambahkan user ke program WillyWangky

# TODO

# KAMUS

# definisi fungsi dan prosedur
# function signup (User : Array[0..CONST_VARS.N-1] of array[0..7] of string) 
# --> Array[0..CONST_VARS.N-1] of array[0..7] of string, integer
# fungsi akan mendaftarkan pemain baru lalu menyimpannya di database user

# ALGORITMA UTAMA
# Loading library
import B01, CONST_VARS

# Realisasi prosedur dan fungsi
def signup(User):
    # KAMUS LOKAL
    # Nama, TanggalLahir, TinggiBadan, Username, Password : string
    # InfoUser, row : array[0..7] of string
    # UsernameList : array[0..CONST_VARS.N-1] of string
    # IndexUser, i : integer

    # ALGORITMA FUNGSI
    # Inisialisasi dictionary
    InfoUser = [' ' for j in range(8)]
    UsernameList = [' ' for j in range(CONST_VARS.N)]

    # Mengisi UsernameList
    i = 1
    for j in  range(CONST_VARS.N):
        row = User[j]
        UsernameList[i] = row[3]
        i += 1
        if (row == CONST_VARS.MARK_8): 
            break

    # Menerima informasi pengguna
    Nama = input("Masukkan nama pemain: ")
    TanggalLahir = input("Masukkan tanggal lahir pemain (DD/MM/YYYY): ")
    TinggiBadan = input("Masukkan tinggi badan pemain (dalam cm): ")
    Username = input("Masukkan username pemain: ")

    # Memeriksa username sudah digunakan atau belum
    while(Username in UsernameList):
        # Jika username sudah digunakan
        print("Username yang anda masukkan sudah terdaftarkan. Silakan pilih username lain.")
        Username = input("Masukkan username pemain: ")
    # Username tidak ada di UsernameList

    Password = input("Masukkan password pemain: ")
    Password = B01.hash(Password) # hashing password

    # Menambahkan data pengguna baru ke InfoUser
    InfoUser[0] = Nama
    InfoUser[1] = TanggalLahir
    InfoUser[2] = TinggiBadan
    InfoUser[3] = Username
    InfoUser[4] = Password
    InfoUser[5] = "pemain"
    InfoUser[6] = "50000"
    InfoUser[7] = "FALSE"
    
    # Mendapatkan index pemain baru
    IndexUser = 1
    row = User[IndexUser] # First element
    
    while (row != CONST_VARS.MARK_8):
        IndexUser += 1
        row = User[IndexUser] # Next element
    
    # row == CONST_VARS.MARK_8
    
    # Menambahkan InfoUser ke User (database user)
    User[IndexUser] = InfoUser

    # Pesan konfirmasi pengguna sudah berhasil didaftarkan
    print("Pengguna baru sudah didaftarkan! Selamat datang {} dan selamat bermain!".format(Nama))
    
    return User,IndexUser