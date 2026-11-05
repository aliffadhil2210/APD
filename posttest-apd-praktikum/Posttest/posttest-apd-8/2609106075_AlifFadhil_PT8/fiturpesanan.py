import data
from data import orders, galon, kurir
from helper import bersihkan_layar, jeda, minta_angka, tanya_teks, tanya_yakin
from tampilan import tampil_galon
from fiturkurir import cari_kurir_siap
 
def buat_nomor_order():
    nomor_baru = data.nomor_order
    data.nomor_order = data.nomor_order + 1
    return nomor_baru
 
def hitung_total(harga, jumlah):
    return harga * jumlah
 
def cari_order(nomor, status, username=None):
    # cari pesanan berdasarkan no, status, (dan username kalau diisi)
    for o in orders:
        if o["no_pesanan"] == nomor and o["status"] == status:
            if username is None or o["username"] == username:
                return o
    return {}
 
def hitung_pendapatan(daftar, i):
    if i >= len(daftar):
        return 0
    sisa = hitung_pendapatan(daftar, i + 1)
    if daftar[i]["status"] == "Selesai":
        return daftar[i]["total"] + sisa
    return sisa
 
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
        np_input = minta_angka("Masukkan no.pesanan (0 = batal) : ", 0, data.nomor_order)
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
    ada = False
    for o in orders:
        if o["username"] == user_login["username"] and o["status"] == "Diproses":
            print("no.pesanan", o["no_pesanan"], "|", o["merk"], "x", o["jumlah"], "| Lokasi:", o["lokasi"], "| Kurir:", o["nama_kurir"])
            ada = True
    if ada == False:
        print("Belum ada pesananmu bos, gaada yang bisa dibatalin.")
    else:
        np_input = minta_angka("Masukkan no.pesanan (0 = batal) : ", 0, data.nomor_order)
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
        np_input = minta_angka("Masukkan no.pesanan yang selesai (0 = batal) : ", 0, data.nomor_order)
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