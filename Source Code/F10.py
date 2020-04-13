#Clarisa Natalia Edelin 16519420
#F10 Kritik dan Saran
#Menerima kritik dan saran mengenai wahana

#Kamus
#Id_Wahana, kritik_saran : string
# tanggal_laporan  : integer

#Algoritma
def KritikdanSaran (DatabaseKritikSaran,InfoUser):
    Kritiksaran = {}

    #Bagian input
    Id_Wahana = input('Masukkan ID Wahana: ')
    tanggal_laporan = input('Masukkan tanggal pelaporan: ')
    kritik_saran = input('Kritik/saran Anda: ')
    Username = InfoUser['Username']

    # Bagian output
    print('Kritik dan saran Anda kami terima')

    #Memasukan input ke file csv
    Kritiksaran['Username'] = Username
    Kritiksaran['TanggalKritik'] = tanggal_laporan
    Kritiksaran['IDWahana'] = Id_Wahana
    Kritiksaran['IsiKritik'] = kritik_saran

    DatabaseKritikSaran.append(Kritiksaran)

    return DatabaseKritikSaran