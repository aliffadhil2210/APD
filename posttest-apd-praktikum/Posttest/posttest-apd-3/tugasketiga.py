#bismillah
username = "alipadel"
password = "75"

print("==========================================")
print("             U D I N   C E L L            ")
print("     Tempat Top Up Murah, Cepat, Aman     ")
print("==========================================")
print("                LOGIN AKUN                ")
print("==========================================")

username_input = input("  Username : ")
password_input = input("  Password : ")
print("------------------------------------------")

if username_input == username and password_input == password:
    print("Login Berhasil")

    print("\n==========================================")
    print("               MENU TOP UP                ")
    print("==========================================")

    id_player = input("  Apa ID Playermu?  : ")
    print("  Pilihan Game : Genshin Impact / Minecraft / Mobile Legends")
    nama_game = input("  Nama Game  : ")
    print("  Pilihan Kategori : Kecil / Menengah / Besar")
    kategori = input("  Kategori   : ")
    if kategori == "Kecil":
        harga_dasar = 15000
    elif kategori == "Menengah":
        harga_dasar = 50000
    else:
        harga_dasar = 150000

    print("  Pilihan Metode : Pulsa / E-Wallet")
    print(" Pulsa ada admin sebesar Rp 2.500, E-Wallet ada admin sebesar Rp 500")
    metode = input("  Metode     : ")

    biaya_admin = 2500 if metode == "Pulsa" else 500
    total_bayar = harga_dasar + biaya_admin

    print("------------------------------------------")
    print("  TOTAL BAYAR : Rp", total_bayar)
    print("------------------------------------------")

    uang_bayar = int(input("  Masukkan nominal uang : Rp "))
    print("------------------------------------------")

    if uang_bayar < total_bayar:
        print("  Transaksi Gagal Saldo tidak mencukupi")
        print("------------------------------------------")
    else:
        kembalian = uang_bayar - total_bayar

        print("==========================================")
        print("      S T R U K   P E M B E L I A N       ")
        print("==========================================")
        print("  ID Player    :", id_player)
        print("  Nama Game    :", nama_game)
        print("  Kategori     :", kategori)
        print("  Metode Bayar :", metode)
        print("  Harga Top Up : Rp", harga_dasar)
        print("  Biaya Admin  : Rp", biaya_admin)
        print("  Total Bayar  : Rp", total_bayar)
        print("  Uang Dibayar : Rp", uang_bayar)
        print("  Kembalian    : Rp", kembalian)
        print("==========================================")
        print("     Terima kasih, selamat bermain!       ")
        print("==========================================")
else:
    print("  Login Gagal")
    print("==========================================")