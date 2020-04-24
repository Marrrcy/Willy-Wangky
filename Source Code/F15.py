# Anastasia Beatrice Caroline / 16519040
# 07 April 2020
# Program tiket_pemain
# Program akan mengizinkan admin melihat jumlah tiket yang dimiliki pemain

# KAMUS
# CONST_VARS
# tiket_pemain : procedure

# DEFINISI PROSEDUR
import CONST_VARS

def tiket_pemain (KepemilikanTiket,Wahana):
	# KAMUS LOKAL
	# Users : string
	
	# ALGORITMA
	# Menginput username
	Users = input("Masukkan username: ")
	
	# Menampilkan informasi tiket
	print("Riwayat:")
	for i in (CONST_VARS.N):
		if Users == KepemilikanTiket[i][0]:
			Id = KepemilikanTiket[i][1]
			Jumlah = KepemilikanTiket[i][2]
			for j in (CONST_VARS.N):
				if Id==Wahana[j][0]:
					Nama = Wahana[j][1]
					print((Id),"\t|\t",(Nama),"\t|\t",(Jumlah))
