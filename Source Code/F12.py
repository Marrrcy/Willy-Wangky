# Anastasia Beatrice Caroline / 16519040
# 07 April 2020
# Program tambah_wahana
# Program akan menambahkan wahana baru ke dalam manajemen wahana

# KAMUS
# tambah_wahana : function

# DEFINISI FUNGSI
def tambah_wahana(Wahana):
	# KAMUS LOKAL
	# df : dictionary of strings
	# Id, Nama, Harga, Umur, Tinggi : string
	
	# ALGORITMA
	# Inisialisasi dictionary
	df = {}
	
	# Menerima informasi wahana tambahan
	print("Masukkan Informasi Wahana yang ditambahkan:")
	Id = input("Masukkan ID Wahana: ")
	Nama = input("Masukkan Nama Wahana: ")
	Harga = input("Masukkan Harga Tiket: ")
	Umur = input("Batasan umur: ")
	Tinggi = input("Batasan tinggi badan: ")
	
	# df = [(Id),(Nama),(Harga),(Umur),(Tinggi)]
	# IdWahana,NamaWahana,HargaTiket,BatasanUmur,BatasanTinggi
	df["IdWahana"] = Id
	df["NamaWahana"] = Nama
	df["HargaTiket"] = Harga
	df["BatasanUmur"] = Umur
	df["BatasanTinggi"] = Tinggi
	Wahana.append(df)
	# print(Wahana)

	return Wahana
	
	
# User = [["Id","Nama","Harga","Umur","Tinggi"]]

# tambah_wahana(User)
