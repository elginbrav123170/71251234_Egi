namaFile = input("Masukkan nama file: ")
try:
    file = open(namaFile, "r")
except:
    print("File tidak ditemukan")

hitungEmail = dict()

for line in file:
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        hitungEmail[email] = hitungEmail.get(email, 0) + 1

print(hitungEmail)