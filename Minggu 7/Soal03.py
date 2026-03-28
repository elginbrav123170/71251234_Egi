t = int(input("Masukkan Tinggi: "))
l = int(input("Masukkan Lebar: "))
angka = 1
for i in range(t):
    for j in range(angka, angka+l):
        print(angka,end=" ")
        angka += 1
    print()
