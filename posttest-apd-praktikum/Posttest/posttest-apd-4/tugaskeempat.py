USERNAME_BENAR = "alipadel"
PIN_BENAR = "075"       
MAKS_PERCOBAAN = 3
saldo = 1000000
print("======================")
print("SELAMAT DATANG DI ATM")
print("======================")
login_berhasil = False
for percobaan in range(1, MAKS_PERCOBAAN + 1):
    username = input("Username : ")
    pin = input("PIN      : ")
    if username == USERNAME_BENAR and pin == PIN_BENAR:
        login_berhasil = True
        print("\nLogin Berhasil!\n")
        break
    else:
        sisa = MAKS_PERCOBAAN - percobaan
        print(f"Login Gagal! Sisa percobaan: {sisa}\n")
if login_berhasil:
    berjalan = True
    while berjalan:
        print("======================")
        print("    MENU UTAMA ATM")
        print("======================")
        print("  [1] Cek Saldo")
        print("  [2] Tarik Tunai")
        print("  [3] Setor Tunai")
        print("  [4] Keluar")
        print("======================")
        pilihan = input("Pilih menu (1-4) : ")
        print()
        if pilihan == "1":
            print("--- CEK SALDO ---")
            print(f"Saldo Anda saat ini : Rp {saldo:,}"+("."))
        elif pilihan == "2":
            print("--- TARIK TUNAI ---")
            kelipatan = 50000  
            kelipatan_teks = f"{kelipatan:,}"+(".")
            nominal_teks = input("Masukkan nominal penarikan : Rp ")
            if not nominal_teks :
                print("Nominal harus berupa angka!")
            else:
                nominal = int(nominal_teks)
                if nominal <= 0:
                    print("Nominal harus lebih dari 0!")
                elif nominal % kelipatan != 0:
                    print(f"Nominal harus kelipatan Rp {kelipatan_teks}")
                elif nominal > saldo:
                    print("Saldo tidak mencukupi!")
                else:
                    saldo -= nominal
                    print("Transaksi berhasil!")
                    print(f"Nominal ditarik : Rp {nominal:,}"+("."))
                    print(f"Sisa saldo      : Rp {saldo:,}"+("."))
        elif pilihan == "3":
            print("--- SETOR TUNAI ---")
            nominal_teks = input("Masukkan nominal setoran : Rp ")
            if not nominal_teks:
                print("Nominal harus berupa angka!")
            else:
                nominal = int(nominal_teks)
                if nominal <= 0:
                    print("Nominal harus lebih dari 0!")
                elif nominal % 50000 != 0:
                    print("Nominal harus kelipatan Rp 50.000")
                else:
                    saldo += nominal
                    print("Setor tunai berhasil!")
                    print(f"Nominal disetor : Rp {nominal:,}"+("."))
                    print(f"Total saldo     : Rp {saldo:,}"+("."))
        elif pilihan == "4":
            print("Terima kasih telah menggunakan layanan ATM kami!")
            berjalan = False
        else:
            print("Pilihan tidak valid! Masukkan angka 1-4.")
        print()
else:
    print("Akun Anda Terblokir!")