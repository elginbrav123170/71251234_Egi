namaFile = input("Masukkan nama file: ")
try:
    file = open(namaFile, "r")
except:
    print("File tidak ditemukan")

hitungDomain = {}

for line in file:
    if line.startswith("From "):
        words = line.split()
        if len(words) > 1:
            email = words[1]
            domain = email.split("@")[1]
            hitungDomain[domain] = hitungDomain.get(domain, 0) + 1

print(hitungDomain)