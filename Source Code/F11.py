#Clarisa Natalia Edelin 16519420
#F11 Melihat kritik dan saran
#Admin dapat melihat kritik dan saran yang telah dimasukkan

#kamus
#Id_wahana : alfanumerik

from sort import insertion_sort
import CONST_VARS
idwahana = ['' for i in range(CONST_VARS.N)]
idwahanaterurut = ['' for i in range(CONST_VARS.N)]
idwahana_terurut = ['' for i in range(CONST_VARS.N)]

#algoritma
def lihatkritikdansaran (wahana):
    Id_wahana = input('Masukkan ID Wahana: ')

    print('Riwayat: ')

    #menginput Id_wahana dari kolom file ke array baru
    for i in range (CONST_VARS.N):
        idwahana [i] = wahana[i]

    idwahanaterurut = idwahana

    #mengurutkan data secara alfabetis
    idwahana_terurut = insertion_sort((idwahanaterurut),2)

    #mencari kritik dan saran sesuai wahana
    for i in range (CONST_VARS.N):
        if Id_wahana == idwahana_terurut[i][2]:
            print(Id_wahana + "\t|\t" + idwahana_terurut[i][1] + '\t|\t' + idwahana_terurut[i][0] + '\t|\t' + idwahana_terurut[i][3])

