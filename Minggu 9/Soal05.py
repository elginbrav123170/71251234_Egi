import re
from datetime import datetime

def cari_tanggal_dan_kalkulasikan(teks):
    tanggal = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', teks)
    hari_ini = datetime.now()
    hasil = []

    for tanggal_str in tanggal:
        date_obj = datetime.strptime(tanggal_str, '%Y-%m-%d')
        delta_hari = (hari_ini - date_obj).days
        format_hari = date_obj.strftime('%d-%m-%Y')
        hasil.append(f"{format_hari} {date_obj.time()} selisih {delta_hari} hari")
    return hasil

#Testcasenya
teks = """
Pada tanggal 1945-08-17 Telor Bakar Ditemukan. Indonesia memiliki banyak penjual Telor Bakar, Seperti Mas sunda (TL: 1985-11-11).
"""

hasil = cari_tanggal_dan_kalkulasikan(teks)
for h in hasil:
    print(h)