# Anastasia Beatrice Caroline / 16519040
# 06 April 2020
# Program cari
# Program ini akan mencari wahana sesuai persyaratan yang diminta

# KAMUS
# CONST_VARS
# cari : procedure

# DEFINISI PROSEDUR
import CONST_VARS

def cari(Wahana):
	# KAMUS LOKAL
	# Umur, Tinggi, Found : integer
	
	# ALGORITMA
	# Menampilkan pilihan persyaratan
	print("Jenis batasan umur:")
	print("1. Anak-anak (<17 tahun)")
	print("2. Dewasa (>=17 tahun)")
	print("3. Semua umur")
	print()
	print("Jenis batasan tinggi badan:")
	print("1. Lebih dari 170 cm")
	print("2. Tanpa Batasan")
	print()
	
	# Menerima informasi persyaratan
	Umur = int(input("Batasan umur pemain: "))
	while (Umur!=(1)and Umur!=(2)and Umur!=(3)):
		print("Batasan umur tidak valid!")	
		Umur = int(input("Batasan umur pemain: "))
		
	Tinggi = int(input("Batasan tinggi badan: "))
	while (Tinggi!=1)and(Tinggi!=2):
		print("Batasan tinggi badan tidak valid!")
		Tinggi = int(input("Batasan tinggi badan: "))
	print()
	
	# Mengubah persyaratan menyesuaikan database
	if Umur == 1 :
		Umur="anak-anak"
	elif Umur == 2 :
		Umur="dewasa"
	else:
		Umur="semua umur"
		
	if Tinggi == 1:
		Tinggi = ">=170 cm"
	else:
		Tinggi = "tanpa batasan"
	
	# Mencari wahana sesuai dengan persyaratan	
	found=0	
	print("Hasil pencarian: ")
	for i in (CONST_VARS.N):
		if Umur==Wahana[i][3] and Tinggi==Wahana[i][4]:
			print(Wahana[i][0],"|",Wahana[i][1],"|",Wahana[i][2])
			found+=1
	# for i in (CONST_VARS.N):
	# 	if Umur==Wahana[i][3] and Tinggi==Wahana[i][4]:
	# 		print(Wahana[i][0],"\t|\t",Wahana[i][1],"\t|\t",Wahana[i][2])
	# 		found+=1
	if found==0:
		print("Tidak ada wahana yang sesuai dengan pencarian kamu.")
