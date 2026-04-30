def hitungRataRata():
    angka = []

    while True:
        inputan = input("Masukkan angka/ketik done untuk selesai: ")

        if inputan.lower() =="done":
            break

        try:
            nilai = float(inputan)
            angka.append(nilai)
        except ValueError:
            print("Mohon masukkan angka dan done saja")
            
    if len(angka) == 0:
        print("Tidak ada yang bisa di masukkan")
    else:
        rataRata = sum(angka) / len(angka)
        print(f"Rata-rata angka yang dimasukkan adalah {rataRata:.2f}")

hitungRataRata()