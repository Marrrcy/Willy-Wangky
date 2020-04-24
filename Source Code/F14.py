#Clarisa Natalia Edelin 16519420
#F14 Melihat riwayat penggunaan wahana
#Admin dapat melihat riwayat penggunaan wahana

#Kamus

#Algoritma
def lihatriwayatwahana (wahana,user):
    #bagian input username pemain
    Id_wahana = input('Masukkan ID Wahana: ')

    Id_wahana_ygsama = []

    #bagian cek wahana
    for i in range(1000):
        for row in range(Wahana):
            if Id_wahana == row['Id_wahana']: #kalau sama
                Id_wahana_ygsama [i] = row #dimasukin ke array baru


    for i in range(1000):
        return print(Id_wahana_terurut[i])
