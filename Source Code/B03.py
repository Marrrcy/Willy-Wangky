#Clarisa Natalia Edelin 16519420
#B03 Best Wahana
#admin akan memberikan daftar 3 wahana terbaik berdasarkan jumlah tiket yang terjual


#Kamus
#jumlahtiket = di file eksternal yang menyatakan jumlah tiket yang terjual per wahana
#Algoritma
tiketterjual = []
tiketterjualterurut = []
tiketterjual_terurut = []
tiketterjualdarikecilkebesar =[]

def bestwahana (wahana):
    #meinput nilai kolom jumlahtiket dari file ke sebuah array tiketterjual
    for i in range (len(User)):
        tiketterjual.append(User[i]['jumlahtiket'])

    tiketterjualterurut = tiketterjual

    #mengurutkan array dari besar ke kecil
    tiketterjual_terurut = sorted(tiketterjualterurut)

    #mengurutkan dta berdasarkan urutan di array tiketterjual
    for i in range (len(User)):
        for j in range (len(User)):
            if tiketterjualterurut[i]==tiketterjual_terurut[j]:
                tiketterjualdarikecilkebesar.append(User[j])

    #menampilkan 3 wahana terbaik berdasarkan jumlah tiket yang terjual
    for i in range (len(User),len(User)-3,-1):
        return print(row)