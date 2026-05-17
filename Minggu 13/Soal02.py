data = ("Elgin Brav Ekazatia", "71251234", "Mamasa, Sulawesi Barat")
nama, nim, alamat = data
    
print("Data: ", data)
print()

print("NIM    : ", nim)
print("NAMA   : ", nama)
print("ALAMAT : ", alamat)
print()

nimTuple = tuple(nim)
print("NIM: ", nimTuple)
print()

namaDepan = nama.split()[0]
namaDepanMinHurufPertama = namaDepan[1:]
namaDepanTuple = tuple(namaDepanMinHurufPertama)
print("NAMA DEPAN: ", namaDepanTuple)
print()

namaTerbalik = tuple(nama.split()[::-1])
print("NAMA TERBALIK: ", namaTerbalik)