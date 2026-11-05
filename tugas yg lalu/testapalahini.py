# print()
# import math
# print(math.sqrt(100))
# print(math.factorial(5))
# print()

# from datetime import datetime
# print(datetime.now())
# print()

# import calendar as kalender
# print(kalender.calendar(2026))
# print()

# import random
# # Menghasilkan satu bilangan bulat acak dari 1 sampai 5 (inklusif)
# print(random.randint(1, 5))
# # Memilih 1 elemen acak dari list atau string
# buah = ["pisang", "rambutan", "manggis"]
# huruf = "abcd"
# print(random.choice(buah)) # memilih 1 item acak pada list
# print(random.choice(huruf)) # memilih 1 karakter acak pada string
# # Menyusun 4 angka PIN acak menggunakan perulangan
# kumpulan_angka = "0123456789"
# pin_acak = ""
# for i in range(4):
#     pin_acak += random.choice(kumpulan_angka)
# print(pin_acak)
# # Mengacak urutan elemen di dalam list secara langsung
# kartu = ["As Wajik", "3 Hati", "7 Sekop"]
# random.shuffle(kartu)
# print(kartu)
print()

# import inquirer
# # Menyusun daftar pertanyaan menu
# pertanyaan = [
# inquirer.List(
# "menu",
# message="Pilih menu aplikasi",
# choices=["Tambah Data", "Lihat Data", "Keluar"],
# ),
# ]
# # Menampilkan prompt di terminal dan menyimpan hasil pilihan
# jawaban = inquirer.prompt(pertanyaan)
# print(jawaban) # Output berupa Dictionary, misal: {'menu': 'TambahData'}
# print(jawaban["menu"]) # Mengambil nilai berdasarkan key 'menu': Tambah Data
