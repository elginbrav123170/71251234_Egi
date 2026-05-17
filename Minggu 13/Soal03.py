namaFile = input("Masukkan nama file: ")

try:
    with open(namaFile) as file:
        hitungJam = dict()

        for baris in file:
            baris = baris.strip()

            if baris.startswith("From "):
                bagian = baris.split()
                waktu = bagian[5]
                jam = waktu.split(":")[0]
                hitungJam[jam] = hitungJam.get(jam, 0) + 1
        
        for jam in sorted(hitungJam):
            print(jam, hitungJam[jam])

except FileNotFoundError:
    print("File tidak ditemukan.")