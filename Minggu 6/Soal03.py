def ips():
    banyakmatkul = int(input("Masukkan jumlah mata kuliah: "))
    totalSKS = banyakmatkul * 3

    totalNilai = 0
    for i in range(1, banyakmatkul + 1):
        while True:
            nilai = input(f"Masukkan nilai mata kuliah {i} (A/B/C/D): ").upper()

            if nilai == "A":
                bobot = 4
            elif nilai == "B":
                bobot = 3
            elif nilai == "C":
                bobot = 2
            elif nilai == "D":
                bobot = 1
            else:
                print("Nilai mata kuliah tidak valid! Masukkan nilai A/B/C/D.")
                continue

            totalNilai += bobot * 3
            break
    
    ips = totalNilai / totalSKS
    print(f"IPS: {round(ips ,2)}")
ips()