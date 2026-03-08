def cek_angka(a,b,c):
    if ((a + b == c) or (a + c == b) or (c + b == a)) and ((a != b) and (a != c) and (c != b)):
        return True
    return False

a,b,c = int(input()), int(input()), int(input())
print(cek_angka(a,b,c))
