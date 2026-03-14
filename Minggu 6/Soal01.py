def perkalian(a,b):
    hasil = 0
    print(f"{a} x {b} = ", end = " ")

    for i in range(a):
        hasil += b
        if i == a - 1:
            print(b, end = " ")
        else:
            print(b, "+", end = " ")
    print(f"= {hasil}")

perkalian(6,5)
perkalian(7,10)
