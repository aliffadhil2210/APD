from helper import bersihkan_layar, pilih_menu
from autentikasi import register, login
from menu import menu_admin, menu_pelanggan
 
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
            user_login = login()
            if len(user_login) > 0:
                if user_login["role"] == "admin":
                    menu_admin()
                else:
                    menu_pelanggan(user_login)
        else:
            register()
 
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print()
        print("Program dihentikan.")