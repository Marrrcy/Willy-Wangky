# Josep Marcello / 16519170
# 13 April 2020
# Program panjangArray
# Program akan menghitung banyak elemen pada suatu array

# KAMUS
# function panjangArray (arr : array [1..N] of any dataType) --> integer

# ALGORITMA

# Realisasi fungsi dan prosedur
def panjangArray(arr):
    # KAMUS LOKAL
    # count : integer

    # ALGORITMA FUNGSI
    # Inisialisasi variabel
    count = 0

    # Meloop setiap elemen dalam arr untuk menghitung jumlah elemennya
    for i in arr:
        count += 1

    return count