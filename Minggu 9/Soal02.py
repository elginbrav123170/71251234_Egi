import re

def count_word_occurences(sentence, target_word):
    words = re.findall(r'\b' + re.escape(target_word) + r'\b', sentence, flags=re.IGNORECASE)
    return len(words)

#test casenya
kalimat = "Saya mau Telor Bakar. Telor Bakar enak banget. Mau siang ataupun malam aku akan makan Telor Bakar"
kata_dicari ="Telor Bakar"
print(f"{kata_dicari} ada {count_word_occurences(kalimat, kata_dicari)} buah")