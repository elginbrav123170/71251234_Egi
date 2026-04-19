import re
import random
import string

def generate_password_random(pangjang=8):
    karakter = string.ascii_letters + string.digits
    return ''.join(random.choice(karakter) for _ in range(pangjang))

def extract_emails_dan_generate_passwords(teks):
    email = re.findall(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', teks)
    hasil = []
    for ema in email:
        username = ema.split('@')[0]
        password = generate_password_random()
        hasil.append(f"{ema} username: {username} , password: {password}")
    return hasil

teks = """
Franchise / Kemitraan Telur Bakar
Telur Bakar Viral Pusat: kemitraan@telurbakarviral.com
Street Food Indonesia: support@streetfoodindo.com
Franchise Telur Bakar Enak: halo@telurbakarenak.id
"""
hasil = extract_emails_dan_generate_passwords(teks)
for h in hasil:
    print(h)