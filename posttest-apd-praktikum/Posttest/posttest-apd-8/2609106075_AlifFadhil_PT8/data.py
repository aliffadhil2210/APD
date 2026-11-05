users = [
    {"username": "admin", "password": "akuadminkaumember", "role": "admin"},
    {"username": "yanto", "password": "000", "role": "pelanggan"},
]
# daftar galonnya: {merk, harga, stok}
galon = [
    {"merk": "Aqua", "harga": 20000, "stok": 10},
    {"merk": "Le Minerale", "harga": 19000, "stok": 8},
    {"merk": "Club", "harga": 18000, "stok": 5},
    {"merk": "Vit", "harga": 17000, "stok": 0},
    {"merk": "Cleo", "harga": 25000, "stok": 1},
]
# daftar kurirnya: {nama, status}
kurir = [
    {"nama": "Johan", "status": "Sibuk"},
    {"nama": "Nawal", "status": "Siap otw"},
    {"nama": "Pahri", "status": "Siap otw"},
]
# orders : {no_pesanan, username, merk, jumlah, lokasi, nama_kurir, total, status}
orders = []
nomor_order = 1
# TUPLE: pilihan status kurir, kalo sibuk gabisa ngurir
status_kurir = ("Siap otw", "Sibuk")
# batas input angka (biar ga kebablasan)
MAKS_HARGA = 10000000
MAKS_STOK = 1000