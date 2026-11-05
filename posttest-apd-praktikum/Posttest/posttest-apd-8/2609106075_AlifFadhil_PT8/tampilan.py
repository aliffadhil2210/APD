from prettytable import PrettyTable
from data import kurir

def tampil_galon(daftar, hanya_tersedia):
    tabel = PrettyTable()
    tabel.field_names = ["No", "Merk", "Harga", "Stok"]
    for i in range(len(daftar)):
        if hanya_tersedia and daftar[i]["stok"] == 0:
            continue
        tabel.add_row([i + 1, daftar[i]["merk"], daftar[i]["harga"], daftar[i]["stok"]])
    if len(tabel.rows) == 0:
        print("Galon sedang habis semua.")
    else:
        print(tabel)
 
def tampil_kurir():
    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama", "Status"]
    for i in range(len(kurir)):
        tabel.add_row([i + 1, kurir[i]["nama"], kurir[i]["status"]])
    if len(tabel.rows) == 0:
        print("Belum ada kurir.")
    else:
        print(tabel)