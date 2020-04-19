#Clarisa Natalia Edelin 16519420
#F11 Melihat kritik dan saran
#Admin dapat melihat kritik dan saran yang telah dimasukkan

#kamus
#Id_wahana : alfanumerik

idwahana = []
idwahanaterurut = []
idwahana_terurut = []

#algoritma
import CONST_VARS
def lihatkritikdansaran (wahana):
    Id_wahana = input('Masukkan ID Wahana: ')

    print('Riwayat: ')

    #menginput Id_wahana dari kolom file ke array baru
    for i in range (CONST_VARS.N):
        idwahana [i] = wahana[i]['id_wahana']

    idwahanaterurut = idwahana

    #mengurutkan data secara alfabetis
    idwahana_terurut = sorted(idwahanaterurut)

    #mencari kritik dan saran sesuai wahana
    for i in range (CONST_VARS.N):
        if Id_wahana == idwahana_terurut[i] :
            return print(row['tanggal'] + '|' + row['user'] + '|' + row['jumlah_pemain_main_di_wahana'])


