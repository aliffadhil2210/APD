import os
# DATA (NESTED LIST)
# daftar user (yg bisa ngakses): [username, password, role]
users = [
    ["admin", "akuadminkaumember", "admin"],
    ["yanto", "000", "pelanggan"],
]
# daftar galonnya: [merk, harga, stok]
galon = [
    ["Aqua", 20000, 10],
    ["Le Minerale", 19000, 8],
    ["Club", 18000, 5],
    ["Vit", 17000, 0],
]
# daftar kurirnya: [nama, status]
kurir = [
    ["Johan", "Sibuk"],
    ["Nawal", "Siap otw"],
    ["Pahri", "Siap otw"],
]
# orders : [no.pesanan, username, merk, jumlah, lokasi, nama_kurir, status]
orders = []
nomor_order = 1

# TUPLE: pilihan status kurir, kalo sibuk gabisa ngurir
status_kurir = ("Siap otw", "Sibuk")

# DAFTAR ANGKA UNTUK CEK INPUT
# Isinya "1", "2", "3", ... "1000" (berupa teks)
# Jadi kalau pelanggan atau usernya ngetik pake huruf, programnya ga error,
angka = []
for i in range(1, 1001):
    angka.append(str(i))

#PROGRAM UTAMA 
while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("---( Depot Air Galon Lancar Jaya )---")
    print()
    print("1. Login")
    print("2. Buat Akun Baru")
    print("0. Keluar")
    print()
    pilih = input("Pilih menu: ")

    #KELUAR
    if pilih == "0":
        print()
        print("Tengkyu bos!")
        break

    #REGISTER (bikin akun pelanggan)
    elif pilih == "2":
        os.system("cls" if os.name == "nt" else "clear")
        print("---( BUAT AKUN BARU )---")
        print()
        username_baru = input("Username : ")
        password_baru = input("Password : ")

        sudah_ada = False
        for u in users:
            if u[0] == username_baru:
                sudah_ada = True
        if username_baru == "":
            print("Namamu masih kosong bos!")
        elif sudah_ada == True:
            print("Ganti nama lain, udah ada yang make")
        elif len(password_baru) < 3:
            print("Password minimal 3 karakter!")
        else:
            users.append([username_baru, password_baru, "pelanggan"])
            print("Register berhasil bos, silakan login.")
            print()
        input("Tekan Enter...")

    #LOGIN
    elif pilih == "1":
        os.system("cls" if os.name == "nt" else "clear")
        print("---( LOGIN )---")
        print()
        username = input("Username : ")
        password = input("Password : ")

        user_login = []   # kosong = belum ada yang cocok
        for u in users:
            if u[0] == username and u[1] == password:
                user_login = u

        if len(user_login) == 0:
            print("Username atau password salah!")
            input("Tekan Enter...")

        #  MENU ADMIN
        elif user_login[2] == "admin":
            while True:
                os.system("cls" if os.name == "nt" else "clear")
                print("---( Yang Atmin Atmin Aja )---")
                print()
                print("1. Lihat semua pesanan")
                print("2. Kelola galonmu")
                print("3. Kelola kurirmu")
                print("4. Lihat pelangganmu")
                print("5. Selesaikan pesanan")
                print("0. Logout")
                print()
                menu = input("Pilih menunya bos: ")
                if menu == "0":
                    break

                #LIHAT SEMUA PESANAN (READ)
                elif menu == "1":
                    os.system("cls" if os.name == "nt" else "clear")
                    print("---( SEMUA PESANAN )---")
                    print()
                    if len(orders) == 0:
                        print("Belum ada pesanan bos.")
                    for o in orders:
                        print("no.pesanan", o[0], "|", o[1], "|", o[2], "x", o[3], "| Lokasi:", o[4], "| Kurir:", o[5], "|", o[6])
                        print()
                    input("Tekan Enter Bos...")

                # KELOLA GALON
                elif menu == "2":
                    while True:
                        os.system("cls" if os.name == "nt" else "clear")
                        print("---( KELOLA GALONMU )---")
                        print()
                        for i in range(len(galon)):
                            print(i + 1, ".", galon[i][0], "| Rp", galon[i][1], "| Stok:", galon[i][2])
                        print("")
                        print("1. Tambah galon")
                        print("2. Ubah harga dan stok")
                        print("3. Hapus galon")
                        print("0. Kembali")
                        print()
                        sub = input("Pilih bos: ")
                        if sub == "0":
                            break

                        # CREATE
                        elif sub == "1":
                            merk = input("Merk galon : ")
                            harga = input("Harga      : ")
                            stok = input("Stok       : ")

                            # cek harga: semua karakter harus angka
                            harga_benar = True
                            if harga == "":
                                harga_benar = False
                            for huruf in harga:
                                if huruf not in "0123456789":
                                    harga_benar = False
                            if merk == "":
                                print("Merknya jangan kosong lah bos")
                            elif harga_benar == False:
                                print("Harganya harus angka angka bos")
                            elif stok not in angka and stok != "0":
                                print("Stoknya harus angka bos")
                            else:
                                galon.append([merk, int(harga), int(stok)])
                                print("Galonnya udah ditambah bos!")
                            input("Tekan Enter Bos...")

                        # UPDATE
                        elif sub == "2":
                            nomor = input("Nomor galon yang diubah : ")
                            if nomor in angka and int(nomor) <= len(galon):
                                harga = input("Harga baru : ")
                                stok = input("Stok baru  : ")

                                harga_benar = True
                                if harga == "":
                                    harga_benar = False
                                for huruf in harga:
                                    if huruf not in "0123456789":
                                        harga_benar = False

                                if harga_benar == False:
                                    print("Harganya harus pake angka bos")
                                elif stok not in angka and stok != "0":
                                    print("Stoknya harus berupa angka bos")
                                else:
                                    galon[int(nomor) - 1][1] = int(harga)
                                    galon[int(nomor) - 1][2] = int(stok)
                                    print("Data galon udah diubah bos!")
                            else:
                                print("Nomornya salah bos")
                            input("Tekan Enter Bos...")

                        # DELETE
                        elif sub == "3":
                            nomor = input("Nomor galon yang dihapus : ")
                            if nomor in angka and int(nomor) <= len(galon):
                                galon.pop(int(nomor) - 1)
                                print("Galonnya udah dihapus bos!")
                            else:
                                print("Nomornya salah bos")
                            input("Tekan Enter Bos...")
                        else:
                            print("Pilihan tidak valid!")
                            input("Tekan Enter Bos...")

                #KELOLA KURIR
                elif menu == "3":
                    while True:
                        os.system("cls" if os.name == "nt" else "clear")
                        print("---( KELOLA KURIRMU )---")
                        print()
                        for i in range(len(kurir)):
                            print(i + 1, ".", kurir[i][0], "| Status:", kurir[i][1])
                        print("")
                        print("1. Tambah kurir")
                        print("2. Ubah status kurir")
                        print("3. Hapus kurir")
                        print("0. Kembali")
                        print()
                        sub = input("Pilih bos: ")
                        if sub == "0":
                            break

                        # CREATE
                        elif sub == "1":
                            nama = input("Nama kurir : ")
                            nama_ada = False #jaga jaga namanya kedobel
                            for k in kurir:
                                if k[0] == nama:
                                    nama_ada = True
                            if nama == "":
                                print("Mana namanya bos?")
                            elif nama_ada == True:
                                print("Nama kurir sudah ada bos!")
                            else:
                                kurir.append([nama, "Siap otw"])
                                print("Kurir", nama, "udah ditambah!")
                            input("Tekan Enter Bos...")

                        # UPDATE
                        elif sub == "2":
                            nomor = input("Nomor kurir : ")
                            if nomor in angka and int(nomor) <= len(kurir):
                                print("1. Siap otw")
                                print("2. Sibuk")
                                st = input("Pilih status baru : ")
                                if st == "1":
                                    kurir[int(nomor) - 1][1] = status_kurir[0]
                                    print("Kurirnya udah Siap otw.")
                                elif st == "2":
                                    kurir[int(nomor) - 1][1] = status_kurir[1]
                                    print("Kurirnya udah dibuat Sibuk.")
                                else:
                                    print("Pilihan tidak valid!")
                            else:
                                print("Nomor tidak valid!")
                            input("Tekan Enter Bos...")

                        # DELETE
                        elif sub == "3":
                            nomor = input("Nomor kurir yang dihapus : ")
                            if nomor in angka and int(nomor) <= len(kurir):
                                if kurir[int(nomor) - 1][1] == "Sibuk":
                                    print("Kurir masih sibuk bos, gaboleh dihapus!")
                                else:
                                    kurir.pop(int(nomor) - 1)
                                    print("Kurir udah dihapus bos!")
                            else:
                                print("Nomor tidak valid!")
                            input("Tekan Enter Bos...")

                        else:
                            print("Pilihan tidak valid!")
                            input("Tekan Enter Bos...")

                #LIHAT PENGGUNA (READ)
                elif menu == "4":
                    os.system("cls" if os.name == "nt" else "clear")
                    print("---( DAFTAR PENGGUNA )---")
                    for i in range(len(users)):
                        print(i + 1, ".", users[i][0], "(", users[i][2], ")")
                    input("Tekan Enter...")

                #SELESAIKAN PESANAN
                elif menu == "5":
                    os.system("cls" if os.name == "nt" else "clear")
                    print("---( SELESAIKAN PESANAN )---")
                    ada = False
                    for o in orders:
                        if o[6] == "Diproses":
                            print("no.pesanan", o[0], "|", o[1], "|", o[2], "x", o[3], "| Kurir:", o[5])
                            ada = True
                    if ada == False:
                        print("Tidak ada pesanan yang diproses.")
                    else:
                        np_input = input("Masukkan no.pesanan yang selesai : ")
                        ketemu = []
                        if np_input in angka:
                            for o in orders:
                                if o[0] == int(np_input) and o[6] == "Diproses":
                                    ketemu = o
                        if len(ketemu) == 0:
                            print("no.pesanan tidak valid!")
                        else:
                            ketemu[6] = "Selesai"
                            for k in kurir:
                                if k[0] == ketemu[5]:
                                    k[1] = "Siap otw"
                            print("Pesanan selesai. Kurir kembali Siap.")
                    input("Tekan Enter...")

                else:
                    print("Pilihan tidak valid!")
                    input("Tekan Enter...")

        #  MENU PELANGGAN
        else:
            while True:
                os.system("cls" if os.name == "nt" else "clear")
                print("---( MENU PELANGGAN )---")
                print()
                print("Hai,", user_login[0])
                print()
                print("1. Lihat galon tersedia")
                print("2. Lihat kurir yang siap")
                print("3. Buat pesanan")
                print("4. Lihat pesanan saya")
                print("5. Ubah lokasi antar jemput")
                print("6. Batalkan pesanan")
                print("0. Logout")
                print()
                menu = input("Pilih menu: ")
                if menu == "0":
                    break

                #LIHAT GALON (READ)
                elif menu == "1":
                    os.system("cls" if os.name == "nt" else "clear")
                    print("---( GALON TERSEDIA )---")
                    ada = False
                    for g in galon:
                        if g[2] > 0:
                            print("-", g[0], "| Rp", g[1], "| Stok:", g[2])
                            ada = True
                    if ada == False:
                        print("Semua galon sedang habis.")
                    input("Tekan Enter...")

                #LIHAT KURIR SIAP (READ)
                elif menu == "2":
                    os.system("cls" if os.name == "nt" else "clear")
                    print("---( KURIR YANG SIAP )---")
                    ada = False
                    for k in kurir:
                        if k[1] == "Siap otw":
                            print("-", k[0])
                            ada = True
                    if ada == False:
                        print("Belum ada kurir yang siap.")
                    input("Tekan Enter...")

                #BUAT PESANAN (CREATE)
                elif menu == "3":
                    os.system("cls" if os.name == "nt" else "clear")
                    print("---( BUAT PESANAN )---")
                    print()

                    #cari kurir yang siap (ambil yang pertama)
                    kurir_siap = []
                    for k in kurir:
                        if k[1] == "Siap otw" and len(kurir_siap) == 0:
                            kurir_siap = k
                            break
                    if len(kurir_siap) == 0:
                        print("Maaf, belum ada kurir yang siap.")
                    else:
                        for i in range(len(galon)):
                            print(i + 1, ".", galon[i][0], "| Rp", galon[i][1], "| Stok:", galon[i][2])
                        nomor = input("Pilih nomor galon : ")
                        if nomor in angka and int(nomor) <= len(galon):
                            pilihan = galon[int(nomor) - 1]
                            if pilihan[2] == 0:
                                print("Stok galon ini habis, belum ngisi lagi.")
                            else:
                                jumlah = input("Jumlah galon : ")
                                if jumlah in angka and int(jumlah) <= pilihan[2]:
                                    lokasi = input("Lokasi antar jemput : ")
                                    if lokasi == "":
                                        print("Lokasimu masih kosong")
                                    else:
                                        orders.append([nomor_order, user_login[0], pilihan[0], int(jumlah), lokasi, kurir_siap[0], "Diproses"])
                                        pilihan[2] = pilihan[2] - int(jumlah)
                                        kurir_siap[1] = "Sibuk"
                                        total = pilihan[1] * int(jumlah)
                                        print("Pesanan berhasil dibuat!")
                                        print("No.pesanan :", nomor_order)
                                        print("Kurir      :", kurir_siap[0])
                                        print("Total      : Rp", total)
                                        nomor_order = nomor_order + 1
                                else:
                                    print("Jumlah tidak valid atau melebihi stok!")
                        else:
                            print("Nomor galon tidak valid, pilih aja yang tersedia.")
                    input("Tekan Enter...")

                #LIHAT PESANAN SAYA (READ)
                elif menu == "4":
                    os.system("cls" if os.name == "nt" else "clear")
                    print("---(PESANAN SAYA) ---")
                    ada = False
                    for o in orders:
                        if o[1] == user_login[0]:
                            print("no.pesanan", o[0], "|", o[2], "x", o[3], "| Lokasi:", o[4], "| Kurir:", o[5], "|", o[6])
                            ada = True
                    if ada == False:
                        print("Kamu belum punya pesanan.")
                    input("Tekan Enter...")

                #UBAH LOKASI (UPDATE)
                elif menu == "5":
                    os.system("cls" if os.name == "nt" else "clear")
                    print("---(UBAH LOKASI) ---")
                    ada = False
                    for o in orders:
                        if o[1] == user_login[0] and o[6] == "Diproses":
                            print("no.pesanan", o[0], "|", o[2], "x", o[3], "| Lokasi:", o[4])
                            ada = True
                    if ada == False:
                        print("Tidak ada pesanan yang bisa diubah.")
                    else:
                        np_input = input("Masukkan no.pesanan : ")
                        ketemu = []
                        if np_input in angka:
                            for o in orders:
                                if o[0] == int(np_input) and o[1] == user_login[0] and o[6] == "Diproses":
                                    ketemu = o
                        if len(ketemu) == 0:
                            print("no.pesanan tidak valid!")
                        else:
                            lokasi_baru = input("Lokasi baru : ")
                            if lokasi_baru == "":
                                print("Lokasimu masih kosong")
                            else:
                                ketemu[4] = lokasi_baru
                                print("Lokasi berhasil diubah!")
                    input("Tekan Enter...")

                #BATALKAN PESANAN (DELETE)
                elif menu == "6":
                    os.system("cls" if os.name == "nt" else "clear")
                    print("---(BATALKAN PESANAN) ---")
                    ada = False
                    for o in orders:
                        if o[1] == user_login[0] and o[6] == "Diproses":
                            print("no.pesanan", o[0], "|", o[2], "x", o[3], "| Lokasi:", o[4], "| Kurir:", o[5])
                            ada = True
                    if ada == False:
                        print("Belum ada pesananmu bos, gaada yang bisa dibatalin.")
                    else:
                        np_input = input("Masukkan no.pesanan : ")
                        ketemu = []
                        if np_input in angka:
                            for o in orders:
                                if o[0] == int(np_input) and o[1] == user_login[0] and o[6] == "Diproses":
                                    ketemu = o
                        if len(ketemu) == 0:
                            print("no.pesanan tidak valid!")
                        else:
                            yakin = input("Yakin batalkan? (yakin/gajadi) : ")
                            if yakin == "yakin":
                                # kembalikan stok galon
                                for g in galon:
                                    if g[0] == ketemu[2]:
                                        g[2] = g[2] + ketemu[3]
                                # kurir jadi siap lagi
                                for k in kurir:
                                    if k[0] == ketemu[5]:
                                        k[1] = "Siap otw"
                                orders.remove(ketemu)
                                print("Pesanan udah dibatalin.")
                            else:
                                print("Pembatalan gajadi.")
                    input("Tekan Enter...")

                else:
                    print("Pilihan tidak valid!")
                    input("Tekan Enter...")

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter...")