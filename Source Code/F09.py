# Muhammad Fahmi Alamsyah/16519300
# 19 April 2020
# Program Menggunakan Tiket
# Program akan menambah saldo dari pengguna dengan merefund tiket yang ada
import CONST_VARS
from panjangArray import panjangArray

def refund (InfoUser,DatabaseTiket,DatabasePembelian,DatabaseWahana, DatabaseRefund):
    #Menerima informasi user
    IdWahana = input("Masukkan ID wahana: ")
    TanggalPembelian = input("Masukkan tanggal hari ini: ")
    JumlahTiket = int(input("Jumlah tiket yang di-refund: "))

    df_tiket = ['' for i in range(3)]
    df_pembelian = ['' for i in range(4)]

    found = 0
    IndexWahana = 0
    for wahana in DatabaseWahana :
        if(wahana[0] == IdWahana):
            found += 1
            break
        IndexWahana += 1

    if found == 0 :
        print("Tidak ada wahana")
        return InfoUser,DatabaseTiket,DatabasePembelian, DatabaseRefund
        

    found = False
    if InfoUser[7] == "FALSE":
        index = 0
        for row in DatabasePembelian:
            if (row[0] == InfoUser[3] and row[1] == TanggalPembelian and row[2] == IdWahana):
                found = True
                # Uang refund adalah 80% dari harga tiket asli
                InfoUser[6] = int(int(InfoUser[6]) + 0.8 * int(wahana[2]) * JumlahTiket)
                DatabaseTiket[index][2] = int(DatabaseTiket[index][2]) - JumlahTiket
                DatabasePembelian[index][3] = int(DatabasePembelian[index][3]) - JumlahTiket
                print("Uang refund sudah kami berikan pada akun Anda.")
                break
            index += 1

        if not(found):
            print("Anda tidak memiliki tiket terkait.")
            return InfoUser,DatabaseTiket,DatabasePembelian, DatabaseRefund

    else: # gold user
        index = 0
        for row in DatabasePembelian:
            if (row[0] == InfoUser[3] and row[1] == TanggalPembelian and row[2] == IdWahana):
                # Uang refund adalah 80% dari harga tiket asli
                found = True
                InfoUser[6] = int(int(InfoUser[6]) + 0.8 * 0.5 * int(wahana[2]) * JumlahTiket)
                DatabaseTiket[index][2] = int(DatabaseTiket[index][2]) - JumlahTiket
                DatabasePembelian[index][3] = int(DatabasePembelian[index][3]) - JumlahTiket
                print("Uang refund sudah kami berikan pada akun Anda.")
                break
            index += 1

        if not(found):
            print("Anda tidak memiliki tiket terkait.")
            return InfoUser,DatabaseTiket,DatabasePembelian, DatabaseRefund

    if (found):
        df_refund =(InfoUser[3], TanggalPembelian, IdWahana, JumlahTiket)

        IdRfd = 1
        row = DatabaseRefund[IdRfd]

        while row != CONST_VARS.MARK_4:
            IdRfd += 1
            row = DatabaseRefund[IdRfd] # Next element

        DatabaseRefund[IdRfd] = df_refund

        return InfoUser, DatabaseTiket,DatabasePembelian, DatabaseRefund
    # Redundant (mubazir)
    else :
        return InfoUser, DatabaseTiket,DatabasePembelian, DatabaseRefund
            
        
##    # Mendapatkan index untuk entri baru di database tiket
##    IndexTiket = 1
##    row = DatabaseTiket[IndexTiket] # First element
##    
##    while (row != CONST_VARS.MARK_3):
##        IndexTiket += 1
##        row = DatabaseTiket[IndexTiket] # Next element
##    
##    # row == CONST_VARS.MARK_8
##
   # Redundant(Mubazir)
   # Mendapatkan index untuk entri baru di database pembelian
   # IndexRfd = 1
   # row = DatabaseRefund[IndexRfd] # First element
   
   # while (row != CONST_VARS.MARK_4):
       # IndexRfd += 1
       # row = DatabaseRefund[IndexRfd] # Next element
   
   # row == CONST_VARS.MARK_4
            

    df_refund[0] = InfoUser[3]
    df_refund[1] = TanggalRefund
    df_refund[2] = IdWahana
    df_refund[3] = JumlahTiket
    # Menambahkan data baru ke database tiket sementara
    # df_tiket[0] = InfoUser[3]
    # df_tiket[1] = IdWahana
    # df_tiket[2] = JumlahTiket
    
    # Menambahkan data baru ke database pembelian sementara
    # df_pembelian[0] = InfoUser[3]
    # df_pembelian[1] = TanggalPembelian
    # df_pembelian[2] = IdWahana
    # df_pembelian[3] = JumlahTiket

    # menambahkan data bar ke database refund
    DatabaseRefund[IdRfd] = df_refund
    # Menambahkan data baru ke database tiket 
    # DatabaseTiket[IndexTiket] = df_tiket

    # Menambahkan data baru ke database pembelian 
    # DatabasePembelian[IndexPmb] = df_pembelian

    return InfoUser, DatabaseTiket,DatabasePembelian, DatabaseRefund
