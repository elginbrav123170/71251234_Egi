def tigaBilanganTerbaik(bilangan):
    if len(bilangan) < 3:
        raise ValueError("List harus terdiri dari minimal 3 bilangan")
    

    terbaik = list(set(bilangan))
    terbaik.sort(reverse=True)
    print(terbaik)
    return terbaik[:3]

#Test casenya
print(tigaBilanganTerbaik([1,1,9,7,2,4,2,3,4,5]))
