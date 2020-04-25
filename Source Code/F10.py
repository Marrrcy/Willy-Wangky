#Clarisa Natalia Edelin 16519420
#F10 Kritik dan Saran
#Menerima kritik dan saran mengenai wahana

#Kamus
#Id_Wahana, kritik_saran : string
# tanggal_laporan  : integer

#Algoritma
import CONST_VARS

def KritikdanSaran (Kritiksaran,Wahana,InfoUser):
    # KAMUS LOKAL
    # i,index : integer

    #Bagian input
    Id_Wahana = input('Masukkan ID Wahana: ')
    tanggal_laporan = input('Masukkan tanggal pelaporan: ')
    kritik_saran = input('Kritik/saran Anda: ')
    Username = InfoUser[0]

    # Bagian output
    print('Kritik dan saran Anda kami terima')

    # Mencari bagian database yang kosong
    i = 0
    for j  in range(CONST_VARS.N):
        row = Kritiksaran[j]
        if (row == CONST_VARS.MARK_4):
            index = i
            break

        i += 1

    #Memasukan input ke file csv

    Kritiksaran[index][0] = Username  #username urutan ke - 0
    Kritiksaran[index][1] = tanggal_laporan  #tanggalkritik urutan ke - 1
    Kritiksaran[index][2] = Id_Wahana  #IDWahana urutan ke - 2
    Kritiksaran[index][3] = kritik_saran  #IsiKritik urutan ke - 3

    return Kritiksaran

