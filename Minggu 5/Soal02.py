def cek_digit_belakang(a,b,c):
    if (a % 10 == b % 10) or (a % 10 == c % 10) or (b % 10 == c % 10):
        return True
    return False

a,b,c = int(input()), int(input()), int(input())
print(cek_digit_belakang(a,b,c))