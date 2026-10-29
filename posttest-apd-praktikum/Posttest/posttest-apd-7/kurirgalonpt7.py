import os
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
    return
def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")
def jeda():
    input("Tekan Enter...")
def tampil_galon(daftar, hanya_tersedia):
    # cetak daftar galon (nomor = posisi di list)
    ada = False
    for i in range(len(daftar)):
        if hanya_tersedia and daftar[i]["stok"] == 0:
            continue
        print(i + 1, ".", daftar[i]["merk"], "| Rp", daftar[i]["harga"], "| Stok:", daftar[i]["stok"])
        ada = True
    if ada == False:
        print("Galon sedang habis semua.")

def tampil_kurir():
    for i in range(len(kurir)):
        print(i + 1, ".", kurir[i]["nama"], "| Status:", kurir[i]["status"])

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
    username_baru = input("Username : ")
    password_baru = input("Password : ")
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
    username = input("Username : ")
    password = input("Password : ")
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
        print("1. Tambah galon")
        print("2. Ubah harga dan stok")
        print("3. Hapus galon")
        print("0. Kembali")
        print()
        sub = minta_angka("Pilih bos: ", 0, 3)
        if sub == 0:
            break
        # CREATE
        elif sub == 1:
            merk = input("Merk galon : ").strip()
            if merk == "":
                print("Merknya jangan kosong lah bos")
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
def kelola_kurir():
    while True:
        bersihkan_layar()
        print("---( KELOLA KURIRMU )---")
        print()
        tampil_kurir()
        print()
        print("1. Tambah kurir")
        print("2. Ubah status kurir")
        print("3. Hapus kurir")
        print("0. Kembali")
        print()
        sub = minta_angka("Pilih bos: ", 0, 3)
        if sub == 0:
            break
        # CREATE
        elif sub == 1:
            nama = input("Nama kurir : ").strip()
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
                print("1. Siap otw")
                print("2. Sibuk")
                st = minta_angka("Pilih status baru : ", 1, 2)
                kurir[nomor - 1]["status"] = status_kurir[st - 1]
                print("Status kurir udah jadi", status_kurir[st - 1] + ".")
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
def lihat_pengguna():
    bersihkan_layar()
    print("---( DAFTAR PENGGUNA )---")
    for i in range(len(users)):
        print(i + 1, ".", users[i]["username"], "(", users[i]["role"], ")")
    jeda()
def selesaikan_pesanan():
    bersihkan_layar()
    print("---( SELESAIKAN PESANAN )---")
    ada = False
    for o in orders:
        if o["status"] == "Diproses":
            print("no.pesanan", o["no_pesanan"], "|", o["username"], "|", o["merk"], "x", o["jumlah"], "| Kurir:", o["nama_kurir"])
            ada = True
    if ada == False:
        print("Tidak ada pesanan yang diproses.")
    else:
        np_input = minta_angka("Masukkan no.pesanan yang selesai (0 = batal) : ", 0, nomor_order)
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
        print("1. Lihat semua pesanan")
        print("2. Kelola galonmu")
        print("3. Kelola kurirmu")
        print("4. Lihat pelangganmu")
        print("5. Selesaikan pesanan")
        print("0. Logout")
        print()
        menu = minta_angka("Pilih menunya bos: ", 0, 5)
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
        nomor = minta_angka("Pilih nomor galon (0 = batal) : ", 0, len(galon))
        if nomor == 0:
            raise ValueError("Pesanan dibatalkan.")
        pilihan = galon[nomor - 1]
        if pilihan["stok"] == 0:
            raise ValueError("Stok galon ini habis, belum ngisi lagi.")
        jumlah = minta_angka("Jumlah galon : ", 1, pilihan["stok"])
        lokasi = input("Lokasi antar jemput : ").strip()
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
def ubah_lokasi(user_login):
    bersihkan_layar()
    print("---(UBAH LOKASI) ---")
    ada = False
    for o in orders:
        if o["username"] == user_login["username"] and o["status"] == "Diproses":
            print("no.pesanan", o["no_pesanan"], "|", o["merk"], "x", o["jumlah"], "| Lokasi:", o["lokasi"])
            ada = True
    if ada == False:
        print("Tidak ada pesanan yang bisa diubah.")
    else:
        np_input = minta_angka("Masukkan no.pesanan (0 = batal) : ", 0, nomor_order)
        if np_input != 0:
            ketemu = cari_order(np_input, "Diproses", user_login["username"])
            if len(ketemu) == 0:
                print("no.pesanan tidak valid!")
            else:
                lokasi_baru = input("Lokasi baru : ").strip()
                if lokasi_baru == "":
                    print("Lokasimu masih kosong")
                else:
                    ketemu["lokasi"] = lokasi_baru
                    print("Lokasi berhasil diubah!")
    jeda()
def batalkan_pesanan(user_login):
    bersihkan_layar()
    print("---(BATALKAN PESANAN) ---")
    ada = False
    for o in orders:
        if o["username"] == user_login["username"] and o["status"] == "Diproses":
            print("no.pesanan", o["no_pesanan"], "|", o["merk"], "x", o["jumlah"], "| Lokasi:", o["lokasi"], "| Kurir:", o["nama_kurir"])
            ada = True
    if ada == False:
        print("Belum ada pesananmu bos, gaada yang bisa dibatalin.")
    else:
        np_input = minta_angka("Masukkan no.pesanan (0 = batal) : ", 0, nomor_order)
        if np_input != 0:
            ketemu = cari_order(np_input, "Diproses", user_login["username"])
            if len(ketemu) == 0:
                print("no.pesanan tidak valid!")
            else:
                yakin = input("Yakin batalkan? (yakin/gajadi) : ")
                if yakin == "yakin":
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
        print("1. Lihat galon tersedia")
        print("2. Lihat kurir yang siap")
        print("3. Buat pesanan")
        print("4. Lihat pesanan saya")
        print("5. Ubah lokasi antar jemput")
        print("6. Batalkan pesanan")
        print("0. Logout")
        print()
        menu = minta_angka("Pilih menu: ", 0, 6)
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
        print("1. Login")
        print("2. Buat Akun Baru")
        print("0. Keluar")
        print()
        pilih = minta_angka("Pilih menu: ", 0, 2)
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