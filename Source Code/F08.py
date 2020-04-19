# Muhammad Fahmi Alamsyah/16519300
# 19 April 2020
# Program Menggunakan Tiket
# Program akan mengurangi jumlah tiket dari pengguna

def main (InfoUser,DatabaseTiket,DatabaseWahana):
    #Menerima informasi user
    IdWahana = input("Masukkan ID wahana: ")
    TanggalPembelian = input("Masukkan tanggal hari ini: ")
    JumlahTiket = int(input("Jumlah tiket yang dibeli: "))

    found = False
    for wahana in DatabaseWahana[0] :
        if(DatabaseWahana[0] == IdWahana):
            found = True
            break

    if not found :
        print("Tidak ada wahana")

    if JumlahTiket <= int(DatabaseTiket[2]):
       print("Terima kasih telah bermain.")
       DatabaseTiket[2] = str(int(DatabaseTiket[2]) - JumlahTiket)
       
       
    else:
       print("Tiket Anda tidak valid dalam sistem kami")

    return InfoUser,DatabaseTiket,DatabaseWahana