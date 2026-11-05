from data import kurir, status_kurir
from helper import bersihkan_layar, jeda, minta_angka, pilih_menu, tanya_teks
from tampilan import tampil_kurir
 
def cari_kurir_siap():
    for k in kurir:
        if k["status"] == "Siap otw":
            return k
    return {}
 
def kelola_kurir():
    while True:
        bersihkan_layar()
        print("---( KELOLA KURIRMU )---")
        print()
        tampil_kurir()
        print()
        sub = pilih_menu("Pilih bos", [("Tambah kurir", 1), ("Ubah status kurir", 2), ("Hapus kurir", 3), ("Kembali", 0)])
        if sub == 0:
            break
        # CREATE
        elif sub == 1:
            nama = tanya_teks("Nama kurir").strip()
            nama_ada = False  # jaga jaga namanya kedobel
            for k in kurir:
                if k["nama"] == nama:
                    nama_ada = True
            if nama == "":
                print("Mana namanya bos?")
            elif nama_ada == True:
                print("Nama kurir sudah ada bos!")
            else:
                kurir.append({"nama": nama, "status": status_kurir[0]})
                print("Kurir", nama, "udah ditambah!")
            jeda()
        # UPDATE
        elif sub == 2:
            nomor = minta_angka("Nomor kurir (0 = batal) : ", 0, len(kurir))
            if nomor == 0:
                print("Batal ubah.")
            else:
                status_baru = pilih_menu("Pilih status baru", list(status_kurir))
                kurir[nomor - 1]["status"] = status_baru
                print("Status kurir udah jadi", status_baru + ".")
            jeda()
        # DELETE
        else:
            nomor = minta_angka("Nomor kurir yang dihapus (0 = batal) : ", 0, len(kurir))
            if nomor == 0:
                print("Batal hapus.")
            elif kurir[nomor - 1]["status"] == "Sibuk":
                print("Kurir masih sibuk bos, gaboleh dihapus!")
            else:
                kurir.pop(nomor - 1)
                print("Kurir udah dihapus bos!")
            jeda()
 
def lihat_kurir_siap():
    bersihkan_layar()
    print("---( KURIR YANG SIAP )---")
    ada = False
    for k in kurir:
        if k["status"] == "Siap otw":
            print("-", k["nama"])
            ada = True
    if ada == False:
        print("Belum ada kurir yang siap.")
    jeda()