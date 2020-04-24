# Muhammad Fahmi Alamsyah/16519300
# 12 April 2020
# Program Membeli Tiket
# Program akan menambahkan jumlah tiket dari pengguna

import CONST_VARS

def beli_tiket (InfoUser,DatabaseTiket,DatabasePembelian, DatabaseWahana):
    #Menerima informasi user
    IdWahana = input("Masukkan ID wahana: ")
    TanggalPembelian = input("Masukkan tanggal hari ini: ")
    JumlahTiket = int(input("Jumlah tiket yang dibeli: "))

    # df_tiket = {}
    df_tiket = ['' for i in range(3)]
    # df_pembelian = {}
    df_pembelian = ['' for i in range(4)]

    found = 0
    IndexWahana = 0
    for wahana in DatabaseWahana :
        # if(wahana["IdWahana"] == IdWahana):
        if(wahana[0] == IdWahana):
            found += 1
            break
            # break woiiii
        IndexWahana += 1

    if found == 0 :
        print("Tidak ada wahana")
        return InfoUser,DatabaseTiket,DatabasePembelian
        
    # if InfoUser["StatusGold"] == False :
    Umur = int(TanggalPembelian[6:10:])-int(InfoUser[1][6:10:])
    BatasUmur = 0 if (wahana[3] == "semua umur") else 17
    Tinggi = 170 if (wahana[4] == ">=170 cm") else 0
    if InfoUser[7] == "FALSE":
        # if (int(InfoUser["Umur"]) >= int(wahana["BatasUmur"]) and int(InfoUser["Tinggi"]) >= int(wahana["BatasTinggu"]) and  (int(InfoUser["Saldo"]) - wahana["Harga"] * JumlahTiket >= 0)):
        if ((Umur >= BatasUmur) and int(InfoUser[2]) >= Tinggi and  (int(InfoUser[6]) - int(wahana[2]) * JumlahTiket >= 0)):
            InfoUser[6] = str(int(InfoUser[6]) - int(wahana[2]) * JumlahTiket)
            print("Selamat bersenang-senang di {}".format(wahana[1]))
        else :
            print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini.\nSilakan menggunakan wahana lain yang tersedia.")
            return InfoUser, DatabaseTiket,DatabasePembelian

    else:
        if (Umur >= BatasUmur and int(InfoUser[2]) >= Tinggi and  (int(InfoUser[6]) - 0.5 * int(wahana[2]) * JumlahTiket >= 0)):
            print("Selamat bersenang-senang di {}".format(wahana[1]))
            InfoUser[6] = str(int(InfoUser[6]) - 0.5 * int(wahana[2]) * JumlahTiket)
        else :
            print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini.\nSilakan menggunakan wahana lain yang tersedia.")
            return InfoUser, DatabaseTiket,DatabasePembelian
    
    # Mendapatkan index untuk entri baru di database tiket
    IndexTiket = 1
    row = DatabaseTiket[IndexTiket] # First element
    
    while (row != CONST_VARS.MARK_3):
        IndexTiket += 1
        row = DatabaseTiket[IndexTiket] # Next element
    
    # row == CONST_VARS.MARK_3

    # Mendapatkan index untuk entri baru di database pembelian
    IndexPmb = 1
    row = DatabasePembelian[IndexPmb] # First element
    
    while (row != CONST_VARS.MARK_4):
        IndexPmb += 1
        row = DatabasePembelian[IndexPmb] # Next element
    
    # row == CONST_VARS.MARK_4
                                                                    
    # Menambahkan data baru ke database tiket sementara
    df_tiket[0] = InfoUser[3]
    df_tiket[1] = IdWahana
    df_tiket[2] = JumlahTiket
    
    # Menambahkan data baru ke database pembelian sementara
    df_pembelian[0] = InfoUser[3]
    df_pembelian[1] = TanggalPembelian
    df_pembelian[2] = IdWahana
    df_pembelian[3] = JumlahTiket

    # Menambahkan data baru ke database tiket 
    DatabaseTiket[IndexTiket] = df_tiket

    # Menambahkan data baru ke database pembelian 
    DatabasePembelian[IndexPmb] = df_pembelian

    return InfoUser,DatabaseTiket,DatabasePembelian
