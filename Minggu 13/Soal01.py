def semuaSama(t):
    if len(t) <= 1:
        return True
    
    pertama = t[0]

    for elemen in t:
        if elemen != pertama:
            return False
    return True

#test case
tA = (90, 90, 90, 90)
print(semuaSama(tA))
tB = (1, 2, 3, 4)
print(semuaSama(tB))
tC = (10, 10, 11, 12)
print(semuaSama(tC))