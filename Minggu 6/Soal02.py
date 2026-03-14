def ganjar(bawah,atas):
    if bawah < atas:
        if bawah % 2 == 0:
            bawah += 1
        for i in range(bawah, atas, 2):
            print(i, end = " ")
    else:
        if bawah % 2 == 0:
            bawah -= 1
        for i in range(bawah, atas, -2):
            print(i, end = " ")
    print()

ganjar(10, 30)
ganjar(97, 82)