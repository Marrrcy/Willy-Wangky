# Josep Marcello / 16519170
# 8 April 2020
# Program Login
# Untuk login ke program WillyWangky

# TODO

# KAMUS

# Definisi fungsi dan prosedur
# function login(User : Array[0..CONST_VARS.N-1] of array[0..7] of string)
# --> integer

# ALGORITMA
# Memasukakn library yang dibutuhkan
import B01, CONST_VARS

# Realisasi prosedur dan fungsi
def login(User):
    # KAMUS LOKAL
    # LoggedIn : boolean
    # Username, Password : string
    # IndexUser,i : integer
    # UsernameList,PasswordList : array[0..CONST_VARS.N-1] of string
    # row : arrat[0..7] of string

    # ALGORITMA fungsi
    # Inisialisasi variabel
    LoggedIn = False
    UsernameList = [' ' for i in range(CONST_VARS.N)]
    PasswordList = [' ' for i in range(CONST_VARS.N)]

    # Mengisi UsernameList
    i = 1 # first element
    for row in User:
        UsernameList[i] = row[3]
        PasswordList[i] = row[4]
        i += 1 # next element
        if (row == CONST_VARS.MARK_8): 
            break
    
    # row == CCONST_VARS.MARK_8 or row == EOF
    

    # Proses login
    while (not LoggedIn):
        Username = input("Masukkan username: ")
        Password = input("Masukkan password: ")

        # Verifikasi username dan password
        for j in range(i): # Mencari username ada atau tidak, serta mencari indexnya
            if (Username == UsernameList[j]): # Username ditemukan di UsernameList 
                if (B01.check_password(Password,PasswordList[j])): # Pasangan username dan password benar
                    LoggedIn = True
                    IndexUser = j-1
                break
        
        # Jika username tidak ditemukan atau pasangan username dan password tidak cocok
        if (not(LoggedIn)):
            print("Username atau password yang anda masukkan salah!")

    # Pesan konfirmasi pengguna sudah login
    print("Selamat datang kembali {} dan Selamat bermain!".format(User[IndexUser][0]))

    return IndexUser