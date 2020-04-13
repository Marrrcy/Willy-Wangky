# Anastasia Beatrice Caroline / 16519040
# 13 April 2020
# Program tiket_hilang
# Program akan melaporkan kehilangan tiket dan mengganti statusnya menjadi tidak valid

# KAMUS
# tiket_hilang : function

# DEFINISI FUNGSI
def tiket_hilang(KepemilikanTiket,TiketHilang):
	# KAMUS LOKAL
	# Users,Tanggal,Id : string
	# Hilang : integer
	# df : dictionary of strings
	
	# ALGORITMA
	# Menerima informasi
	Users = input("Masukkan username: ")
	Tanggal = input("Tanggal kehilangan tiket: ")
	Id = input("ID wahana: ")
	Hilang = int(input("Jumlah tiket yang dihilangkan: "))
	
	# Mencari data yang sesuai dari database
	for i in KepemilikanTiket:
		if Users == i[0]:
			if Id == i[1]:
				if Hilang <= i[2]:
					# Menambah database Tiket Hilang
					# Inisialisasi dictionary
					df = {}
					
					# df = [(Users),(Tanggal),(Id),(Hilang)]
					# Username,TanggalHilang,IdWahana,BanyakHilang
					df["Username"] = Users
					df["TanggalHilang"] = Tanggal
					df["IdWahana"] = Id
					df["BanyakHilang"] = Hilang
					TiketHilang.append(df)
					# print(TiketHilang)

					# Mengubah database Kepemilikan Tiket
					i[2]-=(Hilang)
				
					# Menyatakan berhasil mengubah data
					print()
					print("Laporan kehilangan tiket Anda telah direkam.")
					return TiketHilang,KepemilikanTiket
							
					
# KepemilikanTiket = [["Username","Id","Jumlah"],
# 					["Keija","A",1],
#					["Keija","B",2]]
					
# TiketHilang = [["Username","Tanggal","Id","Hilang"]]

# tiket_hilang(KepemilikanTiket,TiketHilang)
