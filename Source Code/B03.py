# Clarisa Natalia Edelin 16519420
# B03 Best wahana
# admin akan memberikan daftar 3 wahana terbaik berdasarkan jumlah tiket yang terjual

from sort import insertion_sort
import CONST_VARS

# Kamus
# jumlahtiket = di file eksternal yang menyatakan jumlah tiket yang terjual per wahana
# Algoritma

def bestwahana(pembelian, wahana):
    pembelian = pembelian[1::]

    # mengurutkan csv pembelian berdasarkan ID wahana
    pembelian_terurut_berdasarkanID = [CONST_VARS.MARK_4 for i in range(CONST_VARS.N)]
    pembelian_terurut_berdasarkanID = insertion_sort(pembelian, 2)

    array_id_dan_Jumlahtiket = [CONST_VARS.MARK_3 for i in range(CONST_VARS.N)]

    n = i = m = 0
    nama_wahana = ''
    id_skrg = id_sblm = pembelian_terurut_berdasarkanID[0][2]
    while (n < CONST_VARS.N and pembelian_terurut_berdasarkanID[n] != CONST_VARS.MARK_4):
        sum = 0
        while (id_skrg == id_sblm and pembelian_terurut_berdasarkanID[n] != CONST_VARS.MARK_4):
            sum += int(pembelian_terurut_berdasarkanID[n][3])
            n += 1
            if (n < CONST_VARS.N and pembelian_terurut_berdasarkanID[n] != CONST_VARS.MARK_4):
                id_skrg = pembelian_terurut_berdasarkanID[n][2]  # berikutnya
            else:
                break

        while (m < CONST_VARS.N):
            if id_sblm == wahana[m][0]:  # akses csv wahana untuk ambil nama wahana
                nama_wahana = wahana[m][1]  # akses nama wahana dari filw wahana
            m += 1

        m = 0

        array_id_dan_Jumlahtiket[i] = [id_sblm, nama_wahana, sum]
        if (n < CONST_VARS.N):
            id_skrg = id_sblm = pembelian_terurut_berdasarkanID[n][2]
        else:
            break
        i += 1

        # Id_ygakan_dijumlahkan = pembelian_terurut_berdasarkanID[0][0]  # Idwahana pertama
    # # Id_ygakan_dijumlahkan = pembelian_terurut_berdasarkanID[1][0]  # Idwahana pertama
    # #menjumlahkan tiket yg terjual ke array_id_dan_Jumlahtiket berdasarkan ID wahana
    # for i in range (1000):
    #     for j in range (2):
    #         array_id_dan_Jumlahtiket[i][0] = Id_ygakan_dijumlahkan
    #         while array_id_dan_Jumlahtiket[i][0] == Id_ygakan_dijumlahkan:
    #             array_id_dan_Jumlahtiket[i][1] += pembelian_terurut_berdasarkanID[2][j] #dijumlahkan dengan jumlah tiket yang terjual

    #         Id_ygakan_dijumlahkan = pembelian_terurut_berdasarkanID[j][0] #pindah ke Id wahana berikutnya untuk dicari jumlah tiket yang terjual

    array_id_dan_Jumlahtiket_terurut = insertion_sort(array_id_dan_Jumlahtiket, 2)
    # print hasil array  untuk 3 wahana dengan jumlah tiket terbanyak
    # n = 0
    # while n != 3:
    n = 1
    for i in range(i-1, i-4, -1):
        print(str(n), end=" |\t")
        for j in range(3):
            if (j != 2):
                print(array_id_dan_Jumlahtiket_terurut[i][j], end="\t|\t")
            else:
                print(array_id_dan_Jumlahtiket_terurut[i][j])
        n += 1
