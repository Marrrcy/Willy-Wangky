#Clarisa Natalia Edelin 16519420
#F11 Melihat kritik dan saran
#Admin dapat melihat kritik dan saran yang telah dimasukkan

#kamus
#Id_wahana : alfanumerik

#idwahana = []
#idwahanaterurut = []
#idwahana_terurut = []
import CONST_VARS
from sort import insertion_sort

#algoritma
def lihatkritikdansaran (wahana):
    #Id_wahana = input('Masukkan ID Wahana: ')

    # mengurutkan data secara alfabetis
    idwahana_terurut = insertion_sort((wahana[1::]),2)

    print('Riwayat: ')

    #menginput Id_wahana dari kolom file ke array baru
    #for i in range (1000):
     #   idwahana [i] = user[i]['id_wahana']

    #idwahanaterurut = idwahana

    #mencari kritik dan saran sesuai wahana
    for i in range(CONST_VARS.N):
        row = idwahana_terurut[i]

        if (row == CONST_VARS.MARK_4):
            break

        print(row[2] + '\t|\t' + row[1] + '\t|\t' + row[0] + '\t|\t' + row[3])