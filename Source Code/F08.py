# Muhammad Fahmi Alamsyah/16519300
# 19 April 2020
# Program Menggunakan Tiket
# Program akan mengurangi jumlah tiket dari pengguna

# Kamus
# main : function

# Definisi fungsi
import CONST_VARS

def main (InfoUser,DatabaseTiket,DatabasePembelian,DatabaseWahana,DatabasePenggunaan):
    # Kamus
    # IdWahana : String
    # TanggalPembelian : String
    # JumlahTiket : Integer
    # Found : Boolean

    #Algoritma
    #Menerima informasi user
    IdWahana = input("Masukkan ID wahana: ")
    TanggalPembelian = input("Masukkan tanggal hari ini: ")
    JumlahTiket = int(input("Jumlah tiket yang digunakan: "))

    df_tiket = ['' for i in range(3)]
    df_penggunaan = ['' for i in range(4)]

    found = False
    IndexTiket = 0
    for k in range(CONST_VARS.N):
        tiket = DatabaseTiket[k]
        if(tiket[1] == IdWahana and tiket[0] == InfoUser[3]):
            # Umur = int(TanggalPembelian[6:10:])-int(InfoUser[1][6:10:])
            # Tinggi = 170 if (tiket[4] == ">=170 cm") else 0
            if JumlahTiket <= int(tiket[2]):
                found = True
                print("Terima kasih telah bermain.")
                tiket[2] = str(int(tiket[2]) - JumlahTiket)
                break
            
        IndexTiket += 1

    if found == False :
        print("Tiket Anda tidak valid dalam sistem kami.")
        return InfoUser,DatabaseTiket,DatabasePenggunaan, DatabaseWahana
    
    # Mendapatkan index untuk entri baru di database tiket
    IndexTiket = 1
    row = DatabaseTiket[IndexTiket] # First element
    
    while (row != CONST_VARS.MARK_3):
        IndexTiket += 1
        row = DatabaseTiket[IndexTiket] # Next element
    
    # row == CONST_VARS.MARK_3

    # Mendapatkan index untuk entri baru di database pembelian
    IndexPmb = 1
    row = DatabasePenggunaan[IndexPmb] # First element
    
    while (row != CONST_VARS.MARK_4):
        IndexPmb += 1
        row = DatabasePenggunaan[IndexPmb] # Next element
    
    # row == CONST_VARS.MARK_4
    
    # Menambahkan data baru ke database pembelian sementara
    df_penggunaan[0] = InfoUser[3]
    df_penggunaan[1] = TanggalPembelian
    df_penggunaan[2] = IdWahana
    df_penggunaan[3] = JumlahTiket

    # Menambahkan data baru ke database pembelian 
    DatabasePenggunaan[IndexPmb] = df_penggunaan

    return InfoUser,DatabaseTiket,DatabasePenggunaan,DatabaseWahana
