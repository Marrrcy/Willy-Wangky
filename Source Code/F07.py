# Muhammad Fahmi Alamsyah/16519300
# 12 April 2020
# Program Membeli Tiket
# Program akan menambahkan jumlah tiket dari pengguna

def beli_tiket (InfoUser,DatabaseTiket,DatabasePembelian, DatabaseWahana):
    #Menerima informasi user
    IdWahana = input("Masukkan ID wahana: ")
    TanggalPembelian = input("Masukkan tanggal hari ini: ")
    JumlahTiket = int(input("Jumlah tiket yang dibeli: "))

    df_tiket = {}
    df_pembelian = {}

    found = 0
    for wahana in DatabaseWahana :
        if(wahana["IdWahana"] == IdWahana):
            found += 1
            # break woiiii

    if found == 0 :
        print("Tidak ada wahana")

    # Info aja, ini biar lebih enak diliat, gak harus diubah gini. Komentar ini boleh diapus
    # found = False
    # for wahana in DatabaseWahana:
    #     if(wahana["IdWahana"] == IdWahana):
    #         found True
    #         # break woiiii

    # if not found:
    #     print("Tidak ada wahana")
        
    if InfoUser["StatusGold"] == False :
        if (int(InfoUser["Umur"]) >= int(wahana["BatasUmur"]) and int(InfoUser["Tinggi"]) >= int(wahana["BatasTinggu"]) and  (int(InfoUser["Saldo"]) - wahana["Harga"] * JumlahTiket >= 0)):
            InforUser["Saldo"] = int(InfoUser["Saldo"]) - wahana["Harga"] * JumlahTiket
            print("Selamat bersenang-senang di Almond’s Charm.")

        else :
            print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini.\nSilakan menggunakan wahana lain yang tersedia.")

    else:
        if (int(InfoUser["Umur"]) >= int(wahana["BatasUmur"]) and int(InfoUser["Tinggi"] >= int(wahana["BatasTinggu"]) and  (int(InfoUser["Saldo"]) - 0.5 * wahana["Harga"] * JumlahTiket >= 0))): 
            print("Selamat bersenang-senang di Almond’s Charm")
            InfoUser["Saldo"] = int(InfoUser["Saldo"]) - 0.5 * wahana["Harga"] * JumlahTiket
        else :
            print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini.\nSilakan menggunakan wahana lain yang tersedia.")
                                                                    
           
    df_tiket["Username"] = InfoUser["Username"]
    df_tiket["IdWahana"] = DatabaseWahana["IdWahana"]
    df_tiket["JumlahTiket"] = DatabaseTiket["JumlahTiket"]
    df_pembelian["Username"] = InfoUser["Username"]
    df_pembelian["TanggalPembelian"] = InfoUser["TanggalPembelian"]
    df_pembelian["JumlahTiket"] = DatabaseTiket["JumlahTiket"]
                                                                      
    DatabaseTiket.append(df_tiket)
    DatabasePembelian.appen(df_pembelian)
    return (InfoUser,DatabaseTiket,DatabasePembelian, DatabaseWahana)
