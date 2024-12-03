baris1, baris2 = map(int, input("Masukkan baris1 dan baris2: ").split())
total = 0

for i in range(1, baris1 + 1):
    hasil_baris = 0
    for j in range(i, 0, -1):
        hasil_baris += j * baris2
        print(f"{j}*{baris2}", end="")
        if j > 1:
            print("+", end="")
    print(f"={hasil_baris}")
    total += hasil_baris

print(total)