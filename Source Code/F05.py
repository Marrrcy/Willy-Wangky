# Anastasia Beatrice Caroline / 16519040
# 06 April 2020
# Program cari_pemain
# Program akan mencari data pemain

# KAMUS
# cari_pemain : procedure

# DEFINISI PROSEDUR
def cari_pemain (User):
	# KAMUS LOKAL
	# Users : string
	# found : boolean
	
	# ALGORITMA
	# Menerima informasi
	Users = input("Masukkan username: ")
	
	# Mencari informasi
	found = False
	for i in User:
		if Users == i[3]:
			found = True
			print ("Nama Pemain:",i[0])
			print ("Tinggi Pemain:",i[2])
			print ("Tanggal Lahir Pemain:",i[1])
			break
	# Menampilkan pesan bahwan pemain tidak ditemukan
	if found==False:
		print ("Pemain tidak ditemukan.")

# cari_pemain(User)
