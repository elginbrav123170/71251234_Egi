import string
def kataUnik(namaFile):
    try:
        with open(namaFile, 'r', encoding='utf-8') as file:
            teks = file.read()

        teksBersih = teks.translate(str.maketrans('', '', string.punctuation)).lower()

        kataKata = teksBersih.split()

        kataNonAngka = [kata for kata in kataKata if not kata.isdigit()]

        print("Kata-kata unik dalam artikel:")
        for kata in kataNonAngka:
            print(kata)

    except FileNotFoundError:
        print(f"File '{namaFile}' tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

#test casenya
kataUnik("pacuanKudaInternasional.txt")