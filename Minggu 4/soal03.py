try:
    bulan = int(input("Masukkan bulan (1-12): "))

    if bulan < 1 or bulan > 12:
        print("Bulan yang diinputkan tidak valid. Harus antara 1 dan 12.")
    else:
        if bulan in [1, 3, 5, 7, 8, 10, 12]:
            jumlah_hari = 31
        elif bulan in [4, 6, 9, 11]:
            jumlah_hari = 30
        elif bulan == 2:
            jumlah_hari = 29
        else:
            jumlah_hari = 0

        print(f"Jumlah hari: {jumlah_hari}")

except ValueError:
    print("Input tidak valid. Harap masukkan angka antara 1 dan 12.")