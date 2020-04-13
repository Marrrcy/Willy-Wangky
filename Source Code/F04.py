# Josep Marcello / 16519170
# 8 April 2020
# Program Login
# Untuk login ke program WillyWangky

# TODO
# Definisi fungsi dan prosedur

# KAMUS
# login : function

# Memasukakn library yang dibutuhkan
import B01

# Realisasi prosedur dan fungsi
def login(User,DictionaryPassword):
    # KAMUS LOKAL
    # LoggedIn : Boolean
    # Username, Password : String
    # index : Integer

    # Algoritma fungsi
    # Inisialisasi variabel
    LoggedIn = False

    # Proses login
    while (not LoggedIn):
        Username = input("Masukkan username: ")
        Password = input("Masukkan password: ")

        # Penyocokan username dengan password
        # Username tidak terdaftar
        if not(Username in DictionaryPassword): 
            print("Username atau password salah!")
        # Username dan Password cocok
        # elif (DictionaryPassword[Username] == Password):
        elif (B01.check_password(Password,DictionaryPassword[Username])):
            LoggedIn = True
        # Username dan Password tidak cocok
        else: 
            print("Username atau password salah!")


    # Mencari lokasi user di file user
    for i in range(len(User)):
        if (User[i]['Username'] == Username and LoggedIn): 
            index = i
            break

    # Pesan konfirmasi pengguna sudah login
    print("Selamat datang kembali {}! Selamat bermain.".format(User[index]["Nama"]))
    return True, index

# ALGORITMA