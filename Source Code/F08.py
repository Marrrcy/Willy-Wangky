# Muhammad Fahmi Alamsyah/16519300
# 19 April 2020
# Program Menggunakan Tiket
# Program akan mengurangi jumlah tiket dari pengguna

# Kamus
# main : function

# Definisi fungsi
import CONST_VARS
from panjangArray import panjangArray

def main (InfoUser,DatabaseTiket,DatabasePembelian,DatabaseWahana):
    # Kamus
    # IdWahana : String
    # TanggalPembelian : String
    # JumlahTiket : Integer
    # Found : Boolean

    #Algoritma
    #Menerima informasi user
    IdWahana = input("Masukkan ID wahana: ")
    TanggalPembelian = input("Masukkan tanggal hari ini: ")
    JumlahTiket = int(input("Jumlah tiket yang dibeli: "))

    # df_tiket = {}
    df_tiket = ['' for i in range(3)]
    # df_pembelian = {}
    df_pembelian = ['' for i in range(4)]

    found = False
    IndexWahana = 0
    for wahana in DatabaseWahana :
        if(wahana[0] == IdWahana):
            Umur = int(TanggalPembelian[6:9:])-int(InfoUser[1][6:9:])
            Tinggi = 170 if (wahana[4] == ">=170 cm") else 0
            found = True
            for IndexWahana in range(CONST_VARS.N):
                if JumlahTiket <= DatabaseTiket[2]:
                    print("Terima kasih telah bermain.")
                    DatabaseTiket[2] = DataBaseTiket[2] - JumlahTiket
                    break
                else:
                    print("Tiket Anda tidak valid dalam sistem kami")
                    break
        IndexWahana += 1

    if found == False :
        print("Tidak ada wahana")
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
