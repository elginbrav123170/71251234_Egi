data = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

print("key\tvalue\titem")

i = 1
for key in data:
    print(f"{key}\t{data[key]}\t{i}")
    i += 1