import re

def our_space(kocak):
    return re.sub(r'\s+', ' ', kocak).strip()

#test casenya
kalimat = "Saya    Suka Telor      Bakar    yang bukan      sunda"
print(our_space(kalimat))