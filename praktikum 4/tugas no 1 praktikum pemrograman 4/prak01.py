kelipatan, simbol = input().split()
kelipatan = int(kelipatan)
jumlah_anak = 50

for i in range(1, jumlah_anak + 1):
    if i % kelipatan == 0:
        print(simbol, end=" ")
    else:
        print(i, end=" ")

print()