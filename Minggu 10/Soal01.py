def bandingkan_file(file1, file2):
    lines1 = open(file1).readlines()
    lines2 = open(file2).readlines()

    max_lines = max(len(lines1), len(lines2))

    for i in range(max_lines):
        baris1 = lines1[i].strip() if i < len(lines1) else ''
        baris2 = lines2[i].strip() if i < len(lines2) else ''

        if baris1 != baris2:
            print(f"Perbedaan di baris {i+1}")
            print(f"  File 1:{baris1}")
            print(f"  File 2:{baris2}\n")

#test casenya
bandingkan_file('file1.txt', 'file2.txt')