#Clarisa Natalia Edelin 16519420
#B03 Best Wahana
#admin akan memberikan daftar 3 wahana terbaik berdasarkan jumlah tiket yang terjual


#Kamus
#jumlahtiket = di file eksternal yang menyatakan jumlah tiket yang terjual per wahana
#Algoritma
import CONST_VARS
tiketterjual = []
tiketterjualterurut = []
tiketterjual_terurut = []

def bestwahana (wahana):
    #meinput nilai kolom jumlahtiket dari file ke sebuah array tiketterjual
    for i in range (1000):
        while user[i]['jumlahtiket'] != ',':
            tiketterjual[i] = user[i]['jumlahtiket']

    #mengurutkan array dari besar ke kecil

    tiketterjual_terurut = sorted(tiketterjual)

    #mengurutkan data berdasarkan urutan di array tiketterjual
    for i in range (1,CONST_VARS.N):
        for row in range (Wahana):
            if tiketterjual_terurut[i] == row['jumlahtiket']:
                tiketterjual_terurut[i] = row

    #menampilkan 3 wahana terbaik berdasarkan jumlah tiket yang terjual
    for i in range (CONST_VARS.N-1,CONST_VARS.N-4,-1):
        return print(tiketterjual_terurut[i])


