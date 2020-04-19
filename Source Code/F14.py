#Clarisa Natalia Edelin 16519420
#F14 Melihat riwayat penggunaan wahana
#Admin dapat melihat riwayat penggunaan wahana

#Kamus

#Algoritma
import CONST_VARS

def lihatriwayatwahana (wahana):
    #bagian input ID Wahana
    Id_wahana = input('Masukkan ID Wahana: ')

    Id_wahana_ygsama = []

    #bagian cek wahana
    for i in range(CONST_VARS.N):
        for row in wahana:
            print(row)
            if Id_wahana == row[0]:
                Id_wahana_ygsama [i] = row
        Id_wahana_ygsama [i] = CONST_VARS.MARK_5

    print(Id_wahana_ygsama)

    #bagian urutin
    Id_wahana_terurut = sorted(Id_wahana_ygsama)

    for i in range(1000):
        while Id_wahana_terurut[i] != CONST_VARS.MARK_5:
            print(Id_wahana_terurut[i])
