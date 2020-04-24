# Anastasia Beatrice Caroline / 16519040
# 07 April 2020
# Program tambah_wahana
# Program akan menambahkan wahana baru ke dalam manajemen wahana

# KAMUS
# CONST_VARS
# tambah_wahana : function

# DEFINISI FUNGSI
import CONST_VARS

def tambah_wahana(Wahana):
	# KAMUS LOKAL
	# df : array[0..4] of strings
	# Id, Nama, Harga, Umur, Tinggi : string
	
	# ALGORITMA
	# Inisialisasi dictionary
	df = ['' for i in range(5)]
	
	# Menerima informasi wahana tambahan
	print("Masukkan Informasi Wahana yang ditambahkan:")
	Id = input("Masukkan ID Wahana: ")
	Nama = input("Masukkan Nama Wahana: ")
	Harga = input("Masukkan Harga Tiket: ")
	Umur = input("Batasan umur: ")
	Tinggi = input("Batasan tinggi badan: ")
	
	# df = [(Id),(Nama),(Harga),(Umur),(Tinggi)]
	# IdWahana,NamaWahana,HargaTiket,BatasanUmur,BatasanTinggi
	df[0] = Id
	df[1] = Nama
	df[2] = Harga
	df[3] = Umur
	df[4] = Tinggi
	# Wahana.append(df)
	# Mendapatkan index wahana baru
	Index = 1
	row = Wahana[Index] # First element

	while (row != CONST_VARS.MARK_5):
		Index += 1
		row = Wahana[Index] # Next element

	# row == CONST_VARS.MARK_5

	Wahana[Index] = df

	return Wahana
