# Anastasia Beatrice Caroline / 16519040
# 13 April 2020
# Program tiket_hilang
# Program akan melaporkan kehilangan tiket dan mengganti statusnya menjadi tidak valid

# KAMUS
# CONST_VARS
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
	for i in range(CONST_VARS.N):
		if Users == KepemilikanTiket[i][0]:
			if Id == KepemilikanTiket[i][1]:
				if Hilang <= int(i[2]):
					# Menambah database Tiket Hilang
					# Inisialisasi dictionary
					df = ['' for j in range(4)]
					
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

					# row == CONST_VARS.MARK_4
					
					TiketHilang[Index] = df

					# Mengubah database Kepemilikan Tiket
					KepemilikanTiket[i][2]=int(KepemilikanTiket[i][2])-(Hilang)
				
					# Menyatakan berhasil mengubah data
					print()
					print("Laporan kehilangan tiket Anda telah direkam.")\

					return TiketHilang,KepemilikanTiket

	return TiketHilang,KepemilikanTiket
