# Muhammad Fahmi Alamsyah/16519300
# 19 April 2020
# Program Top Up
# Program akan menambah saldo user

import CONST_VARS

def topup (DatabaseUser):
    #Menerima informasi user
    Username = input("Masukkan username: ")
    Saldo = int(input("Masukkan saldo yang di-top up: "))

    IndexUser = 0
    for i in range(CONST_VARS.N):
        user = DatabaseUser[i]
        if user[3] == Username:
            user[6] = str(int(user[6]) + Saldo)
            print("Top up berhasil. Saldo",Username,"bertambah menjadi",user[6])
            break
        IndexUser += 1
                
    # Mendapatkan index pemain baru
    # IndexUser = 1
    # row = DatabaseUser[IndexUser] # First element

    # while (row != CONST_VARS.MARK_4):
    #     IndexUser += 1
    #     row = DatabaseUser[IndexUser] # Next element

    return DatabaseUser
