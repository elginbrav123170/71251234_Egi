import re

def cari_terpanjang_dan_terpendek(kalimat):
    huruf = re.findall(r'\b\w+\b', kalimat)
    terpendek = min(huruf, key=len)
    terpanjang = max(huruf, key=len)
    return terpendek, terpanjang

#testcasenya
kalimat = "Telor Bakar Adalah Makanann Terenak di dunia"
pendek, panjang = cari_terpanjang_dan_terpendek(kalimat)
print(f"terpendek: {pendek}, terpanjang: {panjang}")