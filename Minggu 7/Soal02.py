import math
n = int(input("Masukkan Nilai n: "))

for i in range(1,n+1):
    kocak = math.factorial(n-i+1)
    print(kocak, end=" ")
    for j in range(n-i+1,0,-1):
        print(j,end=" ")
    print()