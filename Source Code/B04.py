# Anastasia Beatrice Caroline / 16519040
# 13 April 2020
# Program tiket_hilang
# Program akan melaporkan kehilangan tiket dan mengganti statusnya menjadi tidak valid

# KAMUS
# tiket_hilang : function

# DEFINISI FUNGSI
import CONST_VARS

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
				if Hilang <= int(i[2]):
					# Menambah database Tiket Hilang
					# Inisialisasi dictionary
					df = ['' for i in range(4)]
					
					# df = [(Users),(Tanggal),(Id),(Hilang)]
					# Username,TanggalHilang,IdWahana,BanyakHilang
					df[0] = Users
					df[1] = Tanggal
					df[2] = Id
					df[3] = str(Hilang)
					# TiketHilang.append(df)
					# print(TiketHilang)

					# Mendapatkan index wahana baru
					Index = 1
					row = TiketHilang[Index] # First element

					while (row != CONST_VARS.MARK_4):
						Index += 1
						row = TiketHilang[Index] # Next element

					# row == CONST_VARS.MARK_5
					
					TiketHilang[Index] = df

					# Mengubah database Kepemilikan Tiket
					i[2]=int(i[2])-(Hilang)
				
					# Menyatakan berhasil mengubah data
					print()
					print("Laporan kehilangan tiket Anda telah direkam.")\

					return (TiketHilang,KepemilikanTiket)

	return (TiketHilang,KepemilikanTiket)
							
					
# KepemilikanTiket = [["Username","Id","Jumlah"],
# 					["Keija","A",1],
#					["Keija","B",2]]
					
# TiketHilang = [["Username","Tanggal","Id","Hilang"]]

# tiket_hilang(KepemilikanTiket,TiketHilang)
