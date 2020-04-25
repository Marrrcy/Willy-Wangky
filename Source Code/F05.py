# Anastasia Beatrice Caroline / 16519040
# 06 April 2020
# Program cari_pemain
# Program akan mencari data pemain

# KAMUS
# CONST_VARS
# cari_pemain : procedure

# DEFINISI PROSEDUR
import CONST_VARS

def cari_pemain (User):
	# KAMUS LOKAL
	# Users : string
	# found : boolean
	
	# ALGORITMA
	# Menerima informasi
	Users = input("Masukkan username: ")
	
	# Mencari informasi
	found = False
	for i in range(CONST_VARS.N):
		if Users == User[i][3]:
			found = True
			print ("Nama Pemain:",User[i][0])
			print ("Tinggi Pemain:",User[i][2])
			print ("Tanggal Lahir Pemain:",User[i][1])
			break
	# Menampilkan pesan bahwan pemain tidak ditemukan
	if found==False:
		print ("Pemain tidak ditemukan.")

# cari_pemain(User)
