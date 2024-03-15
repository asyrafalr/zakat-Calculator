
nama_muzaki = []        # Nama orang yang wajib berzakat karena memiliki harta yg melebihi berukuran tertentu
zakat = []				# zakat yang harus dibayarkan
gaji = []				# penghasilan dalam sebulan
nisab = []              # Batasan minimal harta yang diwajibkan dikenakan zakat berdasarkan harga 85 gram emas
haul = 12              # Jangka waktu dimana harta wajib untuk dikeluarkan zakatnya. dalam waktu 1 tahun / atau 12 bulan
penghasilan_tahun = []	# jumlah penghasilan dalam setahun
penghasilan_bulan = []	# untuk perhitungan jumlah penghasilan dalam sebulan
emas = []				# harga per tanggal 4 maret 1160000
uang = []
aset = []
hutang = []
total = []

def main_menu():

    print('''==================== Kalkulator Zakat =====================\n
                1. Zakat Penghasilan
                2. Zakat Mal
                3. Keluar''')
    choice = input('\nSilahkan pilih salah satu opsi berikut(1/2/3): ')
    return choice


def zakat_penghasilan():
	banyak=int(input('Masukan banyak data yang ingin diinputkan : '))
	print('==========================================')
	try:
		for orang in range(banyak):
			nama = input('Masukkan nama anda:').capitalize()
			nama_muzaki.append(nama)
			
			penghasilan = input('Masukkan penghasilan dalam per bulan : ')
			gaji.append(penghasilan)
			
			tahun = 12 * int(gaji[orang])
			penghasilan_tahun.append(tahun)
			
			hitung_zakat = 0.025 * penghasilan_tahun[orang]
			zakat.append(hitung_zakat)
			
			bulan = zakat[orang] / 12
			penghasilan_bulan.append(bulan)
			harga_emas = input('Masukkan harga emas per gram saat ini:')
			nisab_85 = 85 * int(harga_emas)
			nisab.append(nisab_85)
			
			print('='*60)
			print(f'Zakat Penghasilan {nama_muzaki[orang]}')
			print('='*60)
			print(f'Nama                        :{nama_muzaki[orang]}')
			print(f'Penghasilan per bulan       :Rp.{gaji[orang]}')
			print(f'Penghasilan per tahun       :Rp.{penghasilan_tahun[orang]}')
			print(f'Harga nisab (85 gram emas)  :Rp.{nisab[orang]}')
			print(f'Zakat penghasilan           :2.5% * {penghasilan_tahun[orang]} = Rp.{zakat[orang]:.2f}\n')

			if penghasilan_tahun[orang] >= nisab[orang]:
				print(f'Keterangan              : Anda diwajibkan melakukan Zakat penghasilan sebesar Rp.{zakat[orang]:.2f}/tahun')
				print(f'                          atau Rp.{penghasilan_bulan[orang]:.2f}/bulan')
				print('')
			if penghasilan_tahun[orang] <= nisab[orang]:
				print('Keterangan               : Anda tidak diwajibkan untuk membayar Zakat penghasilan karena belum memenuhi nisab')
	except Exception as x :
		print('Mohon masukkan sesuai input yang diminta',x)

def zakat_penghasilan_freelance():
	banyak=int(input('Masukan banyak data yang ingin diinputkan : '))
	print('==========================================')
	try:
		for orang in range(banyak):
			nama = input('Masukkan nama anda:').capitalize()
			nama_muzaki.append(nama)
			total_gaji = 0
			jumlah_bulan = 12
			for bulan in range(1,jumlah_bulan+1):
				gaji_bulanan = int(input(f"Masukkan gaji untuk bulan ke-{bulan}: "))
				total_gaji += gaji_bulanan

			gaji.append(total_gaji)
			
			hitung_zakat = 0.025 * gaji[orang]
			zakat.append(hitung_zakat)
			harga_emas = input('Masukkan harga emas per gram saat ini:')
			nisab_85 = 85 * int(harga_emas)
			nisab.append(nisab_85)
			
			print('='*60)
			print(f'Zakat Penghasilan {nama_muzaki[orang]}')
			print('='*60)
			print(f'Nama                        :{nama_muzaki[orang]}')
			print(f'Penghasilan per tahun       :Rp.{gaji[orang]}')
			print(f'Harga nisab (85 gram emas)  :Rp.{nisab[orang]}')
			print(f'Zakat penghasilan           :2.5% * {gaji[orang]} = Rp.{zakat[orang]:.2f}\n')

			if gaji[orang] >= nisab[orang]:
				print(f'Keterangan                  : Anda diwajibkan melakukan Zakat penghasilan sebesar Rp.{zakat[orang]:.2f}/tahun')
				print('')
			if gaji[orang] <= nisab[orang]:
				print('Keterangan                   : Anda tidak diwajibkan untuk membayar Zakat penghasilan karena belum memenuhi nisab')
	except Exception as x :
		print('Mohon masukkan sesuai input yang diminta',x)


def zakat_penghasilan_freelance_bulanan():
	try:
		nama = input('Masukkan nama anda:').capitalize()
		gaji_bulanan = int(input('Masukkan penghasilan per bulan: '))
		hitung_zakat = 0.025 * gaji_bulanan
		harga_emas = input('Masukkan harga emas per gram saat ini:')
		nisab_85 = 85 * int(harga_emas)
		nisab_perbulan = nisab_85 / 12
		print('='*60)
		print(f'Zakat Penghasilan {nama}')
		print('='*60)
		print(f'Nama                        :{nama}')
		print(f'Penghasilan per bulan       :Rp.{gaji_bulanan}')
		print(f'Harga nisab (85 gram emas)  :Rp.{nisab_perbulan}')
		print(f'Zakat penghasilan           :2.5% * {gaji_bulanan} = Rp.{hitung_zakat:.2f}\n')
		if gaji_bulanan >= nisab_perbulan:
			print(f'Keterangan              : Anda diwajibkan melakukan Zakat penghasilan sebesar Rp.{hitung_zakat:.2f}')
			print('')
		if gaji_bulanan <= nisab_perbulan:
			print('Keterangan               : Anda tidak diwajibkan untuk membayar Zakat penghasilan karena belum memenuhi nisab')
	except Exception as x :
		print('Mohon masukkan sesuai input yang diminta',x)

def zakat_mal():

	banyak=int(input('Masukan banyak data yang ingin diinputkan : '))
	print('==========================================')
	try:
		for orang in range(banyak):
			nama = input('Masukkan nama anda:').capitalize()
			nama_muzaki.append(nama)
			
			NilaiEmasPerak = int(input('Masukkan nilai emas / perak anda(dalam Rp. Jika tidak ada tulis 0): '))
			emas.append(NilaiEmasPerak)
			
			UangTunai= int(input('Masukkan jumlah uang tunai anda (dalam Rp. Jika tidak ada tulis 0): '))
			UangTabungan= int(input('Masukkan jumlah uang tabungan anda (dalam Rp. Jika tidak ada tulis 0): '))
			UangDeposito= int(input('Masukkan jumlah uang deposito anda (dalam Rp. Jika tidak ada tulis 0): '))
			total_uang = UangTunai + UangTabungan + UangDeposito
			uang.append(total_uang)

			kendaraan= int(input('Masukkan harga kendaraan anda (dalam Rp. Jika tidak ada tulis 0): '))
			rumah= int(input('Masukkan harga rumah anda (dalam Rp. Jika tidak ada tulis 0): '))
			asetlain= int(input('Masukkan harga aset anda yang lainnya (dalam Rp. Jika tidak ada tulis 0): '))
			total_aset = kendaraan + rumah + asetlain
			aset.append(total_aset)

			hutangCicilan =  int(input('Masukkan jumlah cicilan atau hutang anda (dalam Rp. Jika tidak ada tulis 0): '))
			hutang.append(hutangCicilan)

			total_semua = NilaiEmasPerak + total_uang + total_aset - hutangCicilan
			total.append(total_semua)

			hitung_zakat = 0.025 * total[orang]
			zakat.append(hitung_zakat)
			
			harga_emas = input('Masukkan harga emas per gram saat ini:')
			nisab_85 = 85 * int(harga_emas)
			nisab.append(nisab_85)

			kepemilikan = int(input('Masukkan jangka waktu kepemilikan aset-aset tersebut (dalam hitungan bulan) : '))
			if kepemilikan < haul:
				print('Anda belum memenuhi persyaratan untuk membayar zakat mal\n')
				continue
			else:		
				print('='*60)
				print(f'{" "*25}Zakat Mal {nama_muzaki[orang]}')
				print('='*60)
				print(f'Nama: {nama_muzaki[orang]}')
				print(f'Nilai emas dan perak: Rp.{emas[orang]}')
				print(f'Uang Tunai, Tabungan, Deposito: Rp.{uang[orang]}')
				print(f'Kendaraan, Rumah, Aset lain: Rp.{aset[orang]}')
				print(f'Hutang/cicilan: Rp.{hutang[orang]}')
				print(f'Harga nisab (85 gram emas)  :Rp.{nisab[orang]}')
				print(f'Zakat Mal: 2.5% * {total[orang]} = Rp.{zakat[orang]:.2f}\n')

				if total[orang] >= nisab[orang]:
					print(f'Keterangan: Anda diwajibkan melakukan Zakat harta/mal sebesar Rp.{zakat[orang]:.2f}\n')

				elif total[orang] <= nisab[orang]:
					print(f'Keterangan: Harta anda tidak memenuhi nisab\n')

	except Exception as x :
		print('Mohon masukkan sesuai input yang diminta',x)

def start():
	while True:
			choice = main_menu()
			if choice == '1':
				print('''==================== Kalkulator Zakat =====================\n
                1. Zakat Penghasilan tetap per tahun
                2. Zakat Penghasilan tidak tetap per tahun
                3. Zakat Penghasilan per bulan''')
				sub_choice = input('Pilihan anda:')
				if sub_choice == '1': 
					zakat_penghasilan()
				elif sub_choice == '2':
					zakat_penghasilan_freelance()
				elif sub_choice == '3':
					zakat_penghasilan_freelance_bulanan()
			elif choice == '2':
				zakat_mal()
			elif choice == '3':
				print('Terima kasih telah menggunakan kalkulator zakat.\njangan lupa berzakat apabila sudah mampu ^^')
				break
			else:
				print('Mohon masukkan input yang benar')
				
start()