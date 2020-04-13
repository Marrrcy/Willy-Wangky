# Anastasia Beatrice Caroline / 16519040
# 06 April 2020
# Program cari
# Program ini akan mencari wahana sesuai persyaratan yang diminta

# KAMUS
# cari : procedure

# DEFINISI PROSEDUR
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
	elif Umur ==2 :
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
	for i in Wahana:
		if Umur==i[3] and Tinggi==i[4]:
			print(i[0],"|",i[1],"|",i[2])
			found+=1
	# for i in Wahana:
	# 	if Umur==i[3] and Tinggi==i[4]:
	# 		print(i[0],"\t|\t",i[1],"\t|\t",i[2])
	# 		found+=1
	if found==0:
		print("Tidak ada wahana yang sesuai dengan pencarian kamu.")
				
# Wahana = [["Id","Nama","Harga","Batas_Umur","Batas_Tinggi"],
#			["A","Aku",10,"anak-anak","tanpa batasan"],
#			["B","Bait",20,"anak-anak",">=170 cm"],
#			["C","Cicak",30,"dewasa",">=170 cm"],
#			["D","Delman",40,"semua umur","tanpa batasan"]]

# cari(Wahana)
