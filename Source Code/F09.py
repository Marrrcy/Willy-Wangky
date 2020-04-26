# Muhammad Fahmi Alamsyah/16519300
# 19 April 2020
# Program Menggunakan Tiket
# Program akan menambah saldo dari pengguna dengan merefund tiket yang ada
import CONST_VARS

def refund (InfoUser,DatabaseTiket,DatabasePembelian,DatabaseWahana, DatabaseRefund):
    #Menerima informasi user
    IdWahana = input("Masukkan ID wahana: ")
    TanggalPembelian = input("Masukkan tanggal hari ini: ")
    JumlahTiket = int(input("Jumlah tiket yang di-refund: "))

    df_tiket = ['' for i in range(3)]
    df_pembelian = ['' for i in range(4)]

    found = 0
    IndexWahana = 0
    for i in range(CONST_VARS.N):
        row = DatabaseWahana[i]
        if(row[0] == IdWahana):
            found += 1
            break
        IndexWahana += 1       

    wahana = row
    found = False
    if InfoUser[7] == "FALSE":
        index = 1
        for i in range(CONST_VARS.N):
            row = DatabasePembelian[i]
            if (row[0] == InfoUser[3] and int(DatabaseTiket[index][2]) >= JumlahTiket and row[2] == IdWahana):
                found = True
                # Uang refund adalah 80% dari harga tiket asli
                InfoUser[6] = int(int(InfoUser[6]) + int(0.8 * int(wahana[2]) * JumlahTiket))
                DatabaseTiket[index][2] = int(DatabaseTiket[index][2]) - JumlahTiket
                DatabasePembelian[index][3] = int(DatabasePembelian[index][3]) - JumlahTiket
                print("Uang refund sudah kami berikan pada akun Anda.")
                break
            index += 1

    else: # gold user
        index = 0
        for i in range(CONST_VARS.N):
            row = DatabasePembelian[i]
            if (row[0] == InfoUser[3] and int(DatabaseTiket[index][2]) >= JumlahTiket and row[2] == IdWahana):
                # Uang refund adalah 80% dari harga tiket asli
                found = True
                InfoUser[6] = int(int(InfoUser[6]) + int(0.8 * 0.5 * int(wahana[2]) * JumlahTiket))
                DatabaseTiket[index][2] = int(DatabaseTiket[index][2]) - JumlahTiket
                DatabasePembelian[index][3] = int(DatabasePembelian[index][3]) - JumlahTiket
                print("Uang refund sudah kami berikan pada akun Anda.")
                break
            index += 1

    if (found):
        df_refund =(InfoUser[3], TanggalPembelian, IdWahana, JumlahTiket)

        IdRfd = 1
        row = DatabaseRefund[IdRfd]

        while row != CONST_VARS.MARK_4:
            IdRfd += 1
            row = DatabaseRefund[IdRfd] # Next element

        DatabaseRefund[IdRfd] = df_refund

        return InfoUser, DatabaseTiket,DatabasePembelian, DatabaseRefund

    else :
        print("Anda tidak memiliki tiket terkait.")
        return InfoUser, DatabaseTiket,DatabasePembelian, DatabaseRefund

            
    # menambahkan data bar ke database refund
    df_refund[0] = InfoUser[3]
    df_refund[1] = TanggalRefund
    df_refund[2] = IdWahana
    df_refund[3] = JumlahTiket

        
    DatabaseRefund[IdRfd] = df_refund

    return InfoUser, DatabaseTiket,DatabasePembelian, DatabaseRefund
