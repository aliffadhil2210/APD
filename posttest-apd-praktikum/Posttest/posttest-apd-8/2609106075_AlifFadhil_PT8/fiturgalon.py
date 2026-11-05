from data import galon, MAKS_HARGA, MAKS_STOK
from helper import bersihkan_layar, jeda, minta_angka, pilih_menu, tanya_teks
from tampilan import tampil_galon
 
def kelola_galon():
    while True:
        bersihkan_layar()
        print("---( KELOLA GALONMU )---")
        print()
        tampil_galon(galon, False)
        print()
        sub = pilih_menu("Pilih bos", [("Tambah galon", 1), ("Ubah harga dan stok", 2), ("Hapus galon", 3), ("Kembali", 0)])
        if sub == 0:
            break
        # CREATE
        elif sub == 1:
            merk = tanya_teks("Merk galon").strip()
            merk_ada = False
            for g in galon:
                if g["merk"].lower() == merk.lower():
                    merk_ada = True
            if merk == "":
                print("Merknya jangan kosong lah bos")
            elif merk_ada:
                print("Merk itu sudah ada bos!")
            else:
                harga = minta_angka("Harga      : ", 0, MAKS_HARGA)
                stok = minta_angka("Stok       : ", 0, MAKS_STOK)
                galon.append({"merk": merk, "harga": harga, "stok": stok})
                print("Galonnya udah ditambah bos!")
            jeda()
        # UPDATE
        elif sub == 2:
            nomor = minta_angka("Nomor galon yang diubah (0 = batal) : ", 0, len(galon))
            if nomor == 0:
                print("Batal ubah.")
            else:
                harga = minta_angka("Harga baru : ", 0, MAKS_HARGA)
                stok = minta_angka("Stok baru  : ", 0, MAKS_STOK)
                galon[nomor - 1]["harga"] = harga
                galon[nomor - 1]["stok"] = stok
                print("Data galon udah diubah bos!")
            jeda()
        # DELETE
        else:
            nomor = minta_angka("Nomor galon yang dihapus (0 = batal) : ", 0, len(galon))
            if nomor == 0:
                print("Batal hapus.")
            else:
                galon.pop(nomor - 1)
                print("Galonnya udah dihapus bos!")
            jeda()
 
def lihat_galon_tersedia():
    bersihkan_layar()
    print("---( GALON TERSEDIA )---")
    tampil_galon(galon, True)
    jeda()