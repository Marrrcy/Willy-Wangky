# Muhammad Fahmi Alamsyah/16519300
# 19 April 2020
# Program Top Up
# Program akan menambah saldo user

import CONST_VARS
from panjangArray import panjangArray

def topup (InfoUser):
    #Menerima informasi user
    Username = input("Masukkan username: ")
    Saldo = int(input("Masukkan saldo yang di-top up: "))

    df_user = ['' for i in range(8)]

    found = False
    for i in InfoUser[0] :
        if(InfoUser[0] == Username):
            found = True
            if(InfoUser[0] == Username):
                InfoUser[6] = str(int(InfoUser[6] + Saldo))
                print("Top up berhasil. Saldo",Username,"bertambah menjadi",InfoUser[6])
                break
        else:
            return InfoUser
    if not found :
        print("Tidak ada username")
        
    # Mendapatkan index pemain baru
    IndexUser = 1
    row = User[IndexUser] # First element

    while (row != CONST_VARS.MARK_8):
        IndexUser += 1
        row = User[IndexUser] # Next element

    return (InfoUser,DatabaseTiket,DatabasePembelian)

    # Menambahkan data saldo baru ke database user
    df_user[0] = Nama
    df_user[1] = TanggalPembelian
    df_user[2] = TinggiBadan
    df_user[3] = Username
    df_user[4] = Password
    df_user[5] = Role
    df_user[6] = Saldo
    df_user[7] = StatusGold
    

    # Menambahkan data baru ke database user
    InfoUser[Saldo] = df_user
