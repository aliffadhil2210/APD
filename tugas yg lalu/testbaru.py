import os
import inquirer
from prettytable import PrettyTable
# daftar user (yg bisa ngakses): {username, password, role}
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

# ---------- HELPER INQUIRER ----------
def pilih_menu(pesan, pilihan):
    hasil = inquirer.prompt([inquirer.List("p", message=pesan, choices=pilihan)])
    if hasil is None:
        raise KeyboardInterrupt
    return hasil["p"]
def tanya_teks(pesan):
    hasil = inquirer.prompt([inquirer.Text("t", message=pesan)])
    if hasil is None:
        raise KeyboardInterrupt
    return hasil["t"]
def tanya_password(pesan):
    hasil = inquirer.prompt([inquirer.Password("t", message=pesan)])
    if hasil is None:
        raise KeyboardInterrupt
    return hasil["t"]
def tanya_yakin(pesan):
    hasil = inquirer.prompt([inquirer.Confirm("y", message=pesan, default=False)])
    if hasil is None:
        raise KeyboardInterrupt
    return hasil["y"]
def pilih_galon(pesan):
    pilihan = []
    for i in range(len(galon)):
        g = galon[i]
        pilihan.append((g["merk"] + " | Rp " + str(g["harga"]) + " | Stok: " + str(g["stok"]), i))
    pilihan.append(("Batal", -1))
    return pilih_menu(pesan, pilihan)
def pilih_kurir(pesan):
    pilihan = []
    for i in range(len(kurir)):
        pilihan.append((kurir[i]["nama"] + " | " + kurir[i]["status"], i))
    pilihan.append(("Batal", -1))
    return pilih_menu(pesan, pilihan)
def pilih_order(pesan, daftar):
    # return no_pesanan, atau 0 kalau batal
    pilihan = []
    for o in daftar:
        label = "No." + str(o["no_pesanan"]) + " | " + o["username"] + " | " + o["merk"] + " x " + str(o["jumlah"]) + " | Lokasi: " + o["lokasi"]
        pilihan.append((label, o["no_pesanan"]))
    pilihan.append(("Batal", 0))
    return pilih_menu(pesan, pilihan)

def cari_kurir_siap():
    for k in kurir:
        if k["status"] == "Siap otw":
            return k
    return {}
def buat_nomor_order():
    global nomor_order
    nomor_baru = nomor_order
    nomor_order = nomor_order + 1
    return nomor_baru
def cari_user(username, password):
    for u in users:
        if u["username"] == username and u["password"] == password:
            return u
    return {}
def hitung_total(harga, jumlah):
    return harga * jumlah
def cari_order(nomor, status, username=None):
    # cari pesanan berdasarkan no, status, (dan username kalau diisi)
    for o in orders:
        if o["no_pesanan"] == nomor and o["status"] == status:
            if username is None or o["username"] == username:
                return o
    return {}
def minta_angka(pesan, minimum, maksimum):
    teks = input(pesan).strip()
    try:
        if not teks.isdecimal():
            raise ValueError("Harus berupa angka bulat bos!")
        nilai = int(teks)
        if nilai < minimum or nilai > maksimum:
            raise ValueError("Angkanya harus antara " + str(minimum) + " sampai " + str(maksimum) + " bos!")
    except ValueError as e:
        print(e)
        return minta_angka(pesan, minimum, maksimum)
    else:
        return nilai
def hitung_pendapatan(daftar, i):
    if i >= len(daftar):
        return 0
    sisa = hitung_pendapatan(daftar, i + 1)
    if daftar[i]["status"] == "Selesai":
        return daftar[i]["total"] + sisa
    return sisa
def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")
def jeda():
    input("Tekan Enter...")
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

def validasi_akun(username, password):
    # raise ValueError kalau akun tidak memenuhi syarat
    if username == "":
        raise ValueError("Namamu masih kosong bos!")
    for u in users:
        if u["username"] == username:
            raise ValueError("Ganti nama lain, udah ada yang make")
    if len(password) < 3:
        raise ValueError("Password minimal 3 karakter!")

# ---------- REGISTER & LOGIN ----------
def register():
    bersihkan_layar()
    print("---( BUAT AKUN BARU )---")
    print()
    username_baru = tanya_teks("Username")
    password_baru = tanya_password("Password")
    try:
        validasi_akun(username_baru, password_baru)
    except ValueError as e:
        print(e)
    else:
        users.append({"username": username_baru, "password": password_baru, "role": "pelanggan"})
        print("Register berhasil bos, silakan login.")
    finally:
        jeda()
def login():
    bersihkan_layar()
    print("---( LOGIN )---")
    print()
    username = tanya_teks("Username")
    password = tanya_password("Password")
    user_login = cari_user(username, password)
    if len(user_login) == 0:
        print("Username atau password salah!")
        jeda()
    elif user_login["role"] == "admin":
        menu_admin()
    else:
        menu_pelanggan(user_login)
# ---------- ADMIN ----------
def lihat_semua_pesanan():
    bersihkan_layar()
    print("---( SEMUA PESANAN )---")
    print()
    if len(orders) == 0:
        print("Belum ada pesanan bos.")
    for o in orders:
        print("no.pesanan", o["no_pesanan"], "|", o["username"], "|", o["merk"], "x", o["jumlah"], "| Lokasi:", o["lokasi"], "| Kurir:", o["nama_kurir"], "| Rp", o["total"], "|", o["status"])
        print()
    print("Pendapatan (pesanan selesai): Rp", hitung_pendapatan(orders, 0))
    jeda()
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
            idx = pilih_galon("Galon yang diubah")
            if idx == -1:
                print("Batal ubah.")
            else:
                harga = minta_angka("Harga baru : ", 0, MAKS_HARGA)
                stok = minta_angka("Stok baru  : ", 0, MAKS_STOK)
                galon[idx]["harga"] = harga
                galon[idx]["stok"] = stok
                print("Data galon udah diubah bos!")
            jeda()
        # DELETE
        else:
            idx = pilih_galon("Galon yang dihapus")
            if idx == -1:
                print("Batal hapus.")
            elif tanya_yakin("Yakin hapus " + galon[idx]["merk"] + "?"):
                galon.pop(idx)
                print("Galonnya udah dihapus bos!")
            else:
                print("Batal hapus.")
            jeda()
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
            idx = pilih_kurir("Kurir yang diubah")
            if idx == -1:
                print("Batal ubah.")
            else:
                status_baru = pilih_menu("Pilih status baru", list(status_kurir))
                kurir[idx]["status"] = status_baru
                print("Status kurir udah jadi", status_baru + ".")
            jeda()
        # DELETE
        else:
            idx = pilih_kurir("Kurir yang dihapus")
            if idx == -1:
                print("Batal hapus.")
            elif kurir[idx]["status"] == "Sibuk":
                print("Kurir masih sibuk bos, gaboleh dihapus!")
            elif tanya_yakin("Yakin hapus " + kurir[idx]["nama"] + "?"):
                kurir.pop(idx)
                print("Kurir udah dihapus bos!")
            else:
                print("Batal hapus.")
            jeda()
def lihat_pengguna():
    bersihkan_layar()
    print("---( DAFTAR PENGGUNA )---")
    for i in range(len(users)):
        print(i + 1, ".", users[i]["username"], "(", users[i]["role"], ")")
    jeda()
def selesaikan_pesanan():
    bersihkan_layar()
    print("---( SELESAIKAN PESANAN )---")
    diproses = []
    for o in orders:
        if o["status"] == "Diproses":
            diproses.append(o)
    if len(diproses) == 0:
        print("Tidak ada pesanan yang diproses.")
    else:
        np_input = pilih_order("Pilih pesanan yang selesai", diproses)
        if np_input != 0:
            ketemu = cari_order(np_input, "Diproses")
            if len(ketemu) == 0:
                print("no.pesanan tidak valid!")
            else:
                ketemu["status"] = "Selesai"
                for k in kurir:
                    if k["nama"] == ketemu["nama_kurir"]:
                        k["status"] = "Siap otw"
                print("Pesanan selesai. Kurir kembali Siap.")
    jeda()
def menu_admin():
    while True:
        bersihkan_layar()
        print("---( Yang Atmin Atmin Aja )---")
        print()
        menu = pilih_menu("Pilih menunya bos", [
            ("Lihat semua pesanan", 1),
            ("Kelola galonmu", 2),
            ("Kelola kurirmu", 3),
            ("Lihat pelangganmu", 4),
            ("Selesaikan pesanan", 5),
            ("Logout", 0),
        ])
        if menu == 0:
            break
        elif menu == 1:
            lihat_semua_pesanan()
        elif menu == 2:
            kelola_galon()
        elif menu == 3:
            kelola_kurir()
        elif menu == 4:
            lihat_pengguna()
        else:
            selesaikan_pesanan()
# ---------- PELANGGAN ----------
def lihat_galon_tersedia():
    bersihkan_layar()
    print("---( GALON TERSEDIA )---")
    tampil_galon(galon, True)
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
def buat_pesanan(user_login):
    bersihkan_layar()
    print("---( BUAT PESANAN )---")
    print()
    kurir_siap = cari_kurir_siap()
    try:
        if len(kurir_siap) == 0:
            raise ValueError("Maaf, belum ada kurir yang siap.")
        tampil_galon(galon, False)
        idx = pilih_galon("Pilih galon")
        if idx == -1:
            raise ValueError("Pesanan dibatalkan.")
        pilihan = galon[idx]
        if pilihan["stok"] == 0:
            raise ValueError("Stok galon ini habis, belum ngisi lagi.")
        jumlah = minta_angka("Jumlah galon : ", 1, pilihan["stok"])
        lokasi = tanya_teks("Lokasi antar jemput").strip()
        if lokasi == "":
            raise ValueError("Lokasimu masih kosong")
    except ValueError as e:
        print(e)
    else:
        no_baru = buat_nomor_order()
        total = hitung_total(pilihan["harga"], jumlah)
        orders.append({"no_pesanan": no_baru, "username": user_login["username"], "merk": pilihan["merk"], "jumlah": jumlah, "lokasi": lokasi, "nama_kurir": kurir_siap["nama"], "total": total, "status": "Diproses"})
        pilihan["stok"] = pilihan["stok"] - jumlah
        kurir_siap["status"] = "Sibuk"
        print("Pesanan berhasil dibuat!")
        print("No.pesanan :", no_baru)
        print("Kurir      :", kurir_siap["nama"])
        print("Total      : Rp", total)
    finally:
        jeda()
def lihat_pesanan_saya(user_login):
    bersihkan_layar()
    print("---(PESANAN SAYA) ---")
    ada = False
    for o in orders:
        if o["username"] == user_login["username"]:
            print("no.pesanan", o["no_pesanan"], "|", o["merk"], "x", o["jumlah"], "| Lokasi:", o["lokasi"], "| Kurir:", o["nama_kurir"], "| Rp", o["total"], "|", o["status"])
            ada = True
    if ada == False:
        print("Kamu belum punya pesanan.")
    jeda()
def pesanan_diproses_user(user_login):
    hasil = []
    for o in orders:
        if o["username"] == user_login["username"] and o["status"] == "Diproses":
            hasil.append(o)
    return hasil
def ubah_lokasi(user_login):
    bersihkan_layar()
    print("---(UBAH LOKASI) ---")
    daftar = pesanan_diproses_user(user_login)
    if len(daftar) == 0:
        print("Tidak ada pesanan yang bisa diubah.")
    else:
        np_input = pilih_order("Pilih pesanan", daftar)
        if np_input != 0:
            ketemu = cari_order(np_input, "Diproses", user_login["username"])
            if len(ketemu) == 0:
                print("no.pesanan tidak valid!")
            else:
                lokasi_baru = tanya_teks("Lokasi baru").strip()
                if lokasi_baru == "":
                    print("Lokasimu masih kosong")
                else:
                    ketemu["lokasi"] = lokasi_baru
                    print("Lokasi berhasil diubah!")
    jeda()
def batalkan_pesanan(user_login):
    bersihkan_layar()
    print("---(BATALKAN PESANAN) ---")
    daftar = pesanan_diproses_user(user_login)
    if len(daftar) == 0:
        print("Belum ada pesananmu bos, gaada yang bisa dibatalin.")
    else:
        np_input = pilih_order("Pilih pesanan yang dibatalkan", daftar)
        if np_input != 0:
            ketemu = cari_order(np_input, "Diproses", user_login["username"])
            if len(ketemu) == 0:
                print("no.pesanan tidak valid!")
            else:
                if tanya_yakin("Yakin batalkan?"):
                    # kembalikan stok galon
                    for g in galon:
                        if g["merk"] == ketemu["merk"]:
                            g["stok"] = g["stok"] + ketemu["jumlah"]
                    # kurir jadi siap lagi
                    for k in kurir:
                        if k["nama"] == ketemu["nama_kurir"]:
                            k["status"] = "Siap otw"
                    orders.remove(ketemu)
                    print("Pesanan udah dibatalin.")
                else:
                    print("Pembatalan gajadi.")
    jeda()
def menu_pelanggan(user_login):
    while True:
        bersihkan_layar()
        print("---( MENU PELANGGAN )---")
        print()
        print("Hai,", user_login["username"])
        print()
        menu = pilih_menu("Pilih menu", [
            ("Lihat galon tersedia", 1),
            ("Lihat kurir yang siap", 2),
            ("Buat pesanan", 3),
            ("Lihat pesanan saya", 4),
            ("Ubah lokasi antar jemput", 5),
            ("Batalkan pesanan", 6),
            ("Logout", 0),
        ])
        if menu == 0:
            break
        elif menu == 1:
            lihat_galon_tersedia()
        elif menu == 2:
            lihat_kurir_siap()
        elif menu == 3:
            buat_pesanan(user_login)
        elif menu == 4:
            lihat_pesanan_saya(user_login)
        elif menu == 5:
            ubah_lokasi(user_login)
        else:
            batalkan_pesanan(user_login)
def main():
    while True:
        bersihkan_layar()
        print("---( Depot Air Galon Lancar Jaya )---")
        print()
        pilih = pilih_menu("Pilih menu", [("Login", 1), ("Buat Akun Baru", 2), ("Keluar", 0)])
        if pilih == 0:
            print()
            print("Tengkyu bos!")
            break
        elif pilih == 1:
            login()
        else:
            register()

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print()
        print("Program dihentikan.")