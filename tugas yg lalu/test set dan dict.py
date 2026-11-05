print()
#
# ini set
# #angka = {1, 2, 3, 6}
#prima = {2, 3, 5, 7}
#print(angka.intersection(prima)) #sama halnya dengan (angka & prima)
#print(angka.difference(prima)) #sama halnya dengan (angka - prima)
#prima.remove(2) #misal angka yg didalam set tidak ada(cth: 4) maka akan muncul error
#print(prima)
#print(prima.discard(2))
#prima.add(7)
#prima.add(11)
#print(prima)
#for item in prima:
#    print(item)

# ini dictionary
kendaraan = {
    'mobil': 'BMW',
    'motor': 'Yamaha',
    'sepeda': 'Polygon',
    'pesawat' : '' #gapapa kosong
    #key   : #value
}
#print(kendaraan['mobil']) #mengambil value dari key mobil
#rint(kendaraan['motor']) #mengambil value dari key motor
#print(kendaraan.get('peda')) #mengambil value dari key sepeda, jika tidak ada maka akan muncul None

#for item in kendaraan:
#    print(item) #menampilkan key dari dictionary
#for item in kendaraan.values():
#    print(item) #menampilkan value dari dictionary
#for item in kendaraan.items():
#    print(item) #menampilkan key dan value dari dictionary
#for key, value in kendaraan.items():
#    print(f"{key} : {value}") #menampilkan key dan value dari dictionary dengan format tertentu

#kendaraan['pesawat'] = 'boeing' #menambahkan key dan value baru kedalam dictionary
#print(kendaraan)
#kendaraan.update({'bus': 'mercedes', 'airbus': 'airbus'}) #bedanya bisa nambah banyak dictionary

#kendaraan['mobil'] = 'Toyota' #mengubah value dari key mobil

#key = input("Masukkan key kendaraan: ")
#kendaraan[key] = 'delman : kuda' #menambahkan key dan value baru kedalam dictionary
#kendaraan.update({'pesawat': 'airbus'}) #mengubah value dari key pesawat
#print(kendaraan)

#print(kendaraan)
#cache = kendaraan.pop('motor') #menghapus key dan value dari dictionary
#print(kendaraan)
#print(kendaraan.get('motor')) #mengambil value dari key motor, jika tidak ada maka akan muncul None
#print(cache) #menampilkan value dari key motor yang sudah dihapus

#del kendaraan['sepeda'] #menghapus key dan value dari dictionary
#print(kendaraan)

#print(kendaraan)
#kendaraan.clear() #menghapus semua key dan value dari dictionary
#print(kendaraan)

#simpan = kendaraan.pop('motor')
#print(simpan) #menampilkan value dari key motor yang sudah dihapus

#print(len(kendaraan)) #menampilkan jumlah key dan value dari dictionary (disini cth:4)


print()