# Anastasia Beatrice Caroline / 16519040
# 07 April 2020
# Program tiket_pemain
# Program akan mengizinkan admin melihat jumlah tiket yang dimiliki pemain

# KAMUS
# tiket_pemain : procedure

# DEFINISI PROSEDUR
def tiket_pemain (KepemilikanTiket,Wahana):
	# KAMUS LOKAL
	# Users : string
	
	# ALGORITMA
	# Menginput username
	Users = input("Masukkan username: ")
	
	# Menampilkan informasi tiket
	print("Riwayat:")
	for i in KepemilikanTiket:
		if Users == i[0]:
			Id = i[1]
			Jumlah = i[2]
			for j in Wahana:
				if Id==j[0]:
					Nama = j[1]
					print((Id),"\t|\t",(Nama),"\t|\t",(Jumlah))
	

# KepemilikanTiket = [["Username","Id","Jumlah"],
# 					["Keija","A",1],
#					["Keija","B",2]]

# Wahana = [["Id","Nama","Harga","Umur","Tinggi"],
# 			["A","Aku",10,"anak-anak","tanpa batasan"],
# 			["B","Bait",20,"anak-anak",">=170 cm"],
#			["C","Cicak",30,"dewasa",">=170 cm"],
#			["D","Delman",40,"semua umur","tanpa batasan"]]

# tiket_pemain(KepemilikanTiket,Wahana)

