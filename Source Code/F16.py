# Josep Marcello / 16519170
# 23 April 2020
# Program exit
# program untuk keluar dari software Willy-Wangky

# KAMUS
# procedure exit(
# dbU : array[0..CONST_VARS.N-1] of array[0..7] of string
# dbW : array[0..CONST_VARS.N-1] of array[0..4] of string
# dbPem : array[0..CONST_VARS.N-1] of array[0..3] of string
# dbPeng : array[0..CONST_VARS.N-1] of array[0..3] of string
# dbT : array[0..CONST_VARS.N-1] of array[0..2] of string
# dbR : array[0..CONST_VARS.N-1] of array[0..3] of string
# dbK : array[0..CONST_VARS.N-1] of array[0..3] of string
# dbTH : array[0..CONST_VARS.N-1] of array[0..3] of string
# loaded : boolean
# ) 

# ALGORITMA
import F02

def exit(dbU, dbW, dbPem, dbPeng, dbT, dbR, dbK, dbTH, loaded):
    # KAMUS LOKAL
    # saveyn : character

    print("Terima kasih telah bermain di Willy Wangky!")
    if (loaded):
        saveyn = input("Ingin Menyimpan file (y/n)? ")

        if (saveyn == 'y' and loaded):
            F02.save(dbU, dbW, dbPem, dbPeng, dbT, dbR, dbK, dbTH)
    
    print("Sedang keluar dari program...")
    print("Sampai bertemu nanti!")