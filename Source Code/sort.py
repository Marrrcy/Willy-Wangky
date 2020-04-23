# 22 April 2020
# Program sort
# Program untuk insertion sort

# Kamus
# function insertion_sort(arr : array[0..CONST_VARS.N] of array string) --> array[0..CONST_VARS.N] of array string

# Algoritma
import CONST_VARS
# fungsi untuk insertion sort
def insertion_sort(matrix,p):
    # KAMUS LOKAL
    # i, j : integer
    # pivot : array

    # ALGORITMA FUNGSI
    for i in range(1,CONST_VARS.N):
        pivot = matrix[i]
        if (pivot[0] == '-'):
            break
        else:
            j = i - 1

            # Memindahakn semua elemen dari [0..i] yang lbh kecil dari pivot
            while (j >= 0 and matrix[j][p] > pivot[p]): # 0 di sini diganti ke yg lain aja; 
                # misalnya mau saldo di database user, nanti jadinya int(matrix[j][6])
                matrix[j+1] = matrix[j]
                j -= 1

            matrix[j+1] = pivot
    
    return matrix