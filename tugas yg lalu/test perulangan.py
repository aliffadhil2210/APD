#batas=10
#for i in range(batas):
#    print(i)

#nilai=[75, 60, 80, 90, 50]
#for elemen in nilai:
#    if elemen >= 70:
#        print(f"lulus dengan nilai {elemen}")
#   else:
#        print(f"tidak lulus nilai {elemen}")

#for i in range(1, 11):
#    print(i)
#for i in range(10, 0, -1):
#    print(i)

#for i in range(1, 3):
#    for j in range(1, 5):
#        print(f"{i} x {j} = {i*j}")

#hitung = 0
#jawab = "ya"
#while(jawab == "ya"):
#    hitung += 1
#    jawab = input ("Mau lanjut?")
#print(f"jumlah perulangan: {hitung}")

#i = 0
#while True:
#    print(i)
#    i += 2
#    if i >= 11:
#        break

#for i in range(10):
#    if i % 2 == 0:
#        continue
#    print(i)

for i in range(20):
    if i == 9:
        break
    elif i % 2 != 0:
        continue
    elif i == 7:
        break
    print(i)
menu = True
while menu:
    print("Menu:")
    print("1. Makan")
    print("2. Minum")
    print("3. Keluar")
    pilihan = input("Pilih menu (1-3): ")