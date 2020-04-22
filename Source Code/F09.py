# Muhammad Fahmi Alamsyah/16519300
# 19 April 2020
# Program Menggunakan Tiket
# Program akan menambah saldo dari pengguna dengan merefund tiket yang ada
import CONST_VARS
from panjangArray import panjangArray

def refund (InfoUser,DatabaseTiket,DatabasePembelian,DatabaseWahana):
    #Menerima informasi user
    IdWahana = input("Masukkan ID wahana: ")
    TanggalPembelian = input("Masukkan tanggal hari ini: ")
    JumlahTiket = int(input("Jumlah tiket yang di-refund: "))

    # df_tiket = {}
    df_tiket = ['' for i in range(3)]
    # df_pembelian = {}
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
        return InfoUser,DatabaseTiket,DatabasePembelian, DatabaseWahana
        

    Umur = int(TanggalPembelian[6:9:])-int(InfoUser[1][6:9:])
    Tinggi = 170 if (wahana[4] == ">=170 cm") else 0
    if InfoUser[7] == "False" :
        if (Umur >= int(wahana[IndexWahana][3]) and int(InfoUser[2]) >= Tinggi and  (int(InfoUser[6]) - int(wahana[IndexWahana][2]) * JumlahTiket >= 0)):
            # Uang refund adalah 80% dari harga tiket asli
            InfoUser[6] = str(int(InfoUser[6]) + 0.8 * int(wahana[2]) * JumlahTiket)
            int(DatabaseTiket[2]) = int(DatabaseTiket[2]) - JumlahTiket
            print("Uang refund sudah kami berikan pada akun Anda.")
            break

        else :
            print("Anda tidak memiliki tiket terkait.")
            return InfoUser,DatabaseTiket,DatabasePembelian, DatabaseWahana

    else:
        if (Umur >= int(wahana[IndexWahana][3]) and int(InfoUser[2]) >= Tinggi and  (int(InfoUser[6]) - 0.5 * int(wahana[IndexWahana][2]) * JumlahTiket >= 0)):
            print("Uang refund sudah kami berikan pada akun Anda.")
            # Uang refund adalah 80% dari harga tiket asli
            InfoUser[6] = str(int(InfoUser[6]) + 0.8 * 0.5 * int(wahana[IndexWahana][2]) * JumlahTiket)
            int(DatabaseTiket[2]) = int(DatabaseTiket[2]) - JumlahTiket
            break
        else :
            print("Anda tidak memiliki tiket terkait.")
            return InfoUser,DatabaseTiket,DatabasePembelian, DatabaseWahana
        
    # Mendapatkan index untuk entri baru di database tiket
    IndexTiket = 1
    row = DatabaseTiket[IndexTiket] # First element
    
    while (row != CONST_VARS.MARK_3):
        IndexTiket += 1
        row = DatabaseTiket[IndexTiket] # Next element
    
    # row == CONST_VARS.MARK_8

    # Mendapatkan index untuk entri baru di database pembelian
    IndexPmb = 1
    row = DatabasePembelian[IndexPmb] # First element
    
    while (row != CONST_VARS.MARK_4):
        IndexPmb += 1
        row = DatabasePembelian[IndexPmb] # Next element
    
    # row == CONST_VARS.MARK_8
                                                                    
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

    return DatabaseTiket,DatabasePembelian
