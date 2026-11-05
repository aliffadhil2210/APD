import os
import inquirer
 
def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")
 
def jeda():
    input("Tekan Enter...")
 
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
 
def pilih_menu(pesan, pilihan):
    # pilihan: list of (label, nilai). Ctrl+C di inquirer -> None -> dihentikan
    hasil = inquirer.prompt([inquirer.List("p", message=pesan, choices=pilihan)])
    if hasil is None:
        raise KeyboardInterrupt
    return hasil["p"]
 
def tanya_teks(pesan, rahasia=False):
    # rahasia=True -> input disembunyikan (buat password)
    if rahasia:
        pertanyaan = inquirer.Password("t", message=pesan)
    else:
        pertanyaan = inquirer.Text("t", message=pesan)
    hasil = inquirer.prompt([pertanyaan])
    if hasil is None:
        raise KeyboardInterrupt
    return hasil["t"]
 
def tanya_yakin(pesan):
    hasil = inquirer.prompt([inquirer.Confirm("y", message=pesan, default=False)])
    if hasil is None:
        raise KeyboardInterrupt
    return hasil["y"]