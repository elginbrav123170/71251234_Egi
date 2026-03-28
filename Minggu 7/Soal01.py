n = int(input("Masukkan nilai n: "))

for i in range(n - 1, 1, -1):
    prima = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            prima = False
            break
    
    if prima == True:
        print(f"Prima terdekat < {n} adalah {i}")
        break