from helper import bersihkan_layar, pilih_menu
from autentikasi import lihat_pengguna
from fiturgalon import kelola_galon, lihat_galon_tersedia
from fiturkurir import kelola_kurir, lihat_kurir_siap
from fiturpesanan import (lihat_semua_pesanan, selesaikan_pesanan, buat_pesanan,lihat_pesanan_saya, ubah_lokasi, batalkan_pesanan)
 
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