# Muhammad Fahmi Alamsyah/16519300
# 19 April 2020
# Program Top Up
# Program akan menambah saldo user

import CONST_VARS
from panjangArray import panjangArray

def topup (InfoUser,DatabaseTiket,DatabasePembelian):
    #Menerima informasi user
    Username = input("Masukkan username: ")
    Saldo = int(input("Masukkan saldo yang di-top up: "))

    found = False
    IndexUser = 0
    for user in InfoUser:
        if user[3] == Username:
            found = True
            InfoUser[6] = str(int(InfoUser[6]) + Saldo)
            print("Top up berhasil. Saldo",Username,"bertambah menjadi",InfoUser[6])
            break
        IndexUser += 1
        
    if not found :
        print("Tidak ada username")
        return InfoUser,DatabaseTiket,DatabasePembelian
        
    # Mendapatkan index pemain baru
    IndexUser = 1
    row = InfoUser[IndexUser] # First element

    while (row != CONST_VARS.MARK_4):
        IndexUser += 1
        row = InfoUser[IndexUser] # Next element

    return (InfoUser,DatabaseTiket,DatabasePembelian)
