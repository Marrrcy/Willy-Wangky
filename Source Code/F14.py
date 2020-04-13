#Clarisa Natalia Edelin 16519420
#F14 Melihat riwayat penggunaan wahana
#Admin dapat melihat riwayat penggunaan wahana

#Kamus

#Algoritma
def lihatriwayatwahana (Wahana,user):
    #bagian input username pemain
    Id_wahana = input('Masukkan ID Wahana: ')


    #bagian cek wahana
    #idwahana adalah nama row di file external
    for row in range (Wahana):
        if Id_wahana == row['Id_wahana']:
            return print(row)
