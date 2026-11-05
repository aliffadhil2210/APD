from data import users
from helper import bersihkan_layar, jeda, tanya_teks
 
def validasi_akun(username, password):
    # raise ValueError kalau akun tidak memenuhi syarat
    if username == "":
        raise ValueError("Namamu masih kosong bos!")
    for u in users:
        if u["username"] == username:
            raise ValueError("Ganti nama lain, udah ada yang make")
    if len(password) < 3:
        raise ValueError("Password minimal 3 karakter!")
 
def cari_user(username, password):
    for u in users:
        if u["username"] == username and u["password"] == password:
            return u
    return {}
 
def register():
    bersihkan_layar()
    print("---( BUAT AKUN BARU )---")
    print()
    username_baru = tanya_teks("Username")
    password_baru = tanya_teks("Password", True)
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
    password = tanya_teks("Password", True)
    user_login = cari_user(username, password)
    if len(user_login) == 0:
        print("Username atau password salah!")
        jeda()
    return user_login
 
def lihat_pengguna():
    bersihkan_layar()
    print("---( DAFTAR PENGGUNA )---")
    for i in range(len(users)):
        print(i + 1, ".", users[i]["username"], "(", users[i]["role"], ")")
    jeda()