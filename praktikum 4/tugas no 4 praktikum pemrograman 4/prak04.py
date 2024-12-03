nama = "afrian pradipta rizky"

while True:
    print("\nPilih program\n")
    print("1. Penjumlahan\n")
    print("2. Pengurangan\n")
    print("3. Perkalian\n")
    print("4. Pembagian\n")
    print("5. Exit\n")
    pilihan = int(input("Masukkan Pilihan : "))

    if pilihan == 1:
        nilai_pertama = float(input("Masukkan nilai pertama : "))
        nilai_kedua = float(input("Masukkan nilai kedua : "))
        hasil = nilai_pertama + nilai_kedua
        print("Hasil penjumlahan antara %.2f dengan %.2f adalah %.2f" % (nilai_pertama, nilai_kedua, hasil))
    elif pilihan == 2:
        nilai_pertama = float(input("Masukkan nilai pertama : "))
        nilai_kedua = float(input("Masukkan nilai kedua : "))
        hasil = nilai_pertama - nilai_kedua
        print("Hasil pengurangan antara %.2f dengan %.2f adalah %.2f" % (nilai_pertama, nilai_kedua, hasil))
    elif pilihan == 3:
        nilai_pertama = float(input("Masukkan nilai pertama : "))
        nilai_kedua = float(input("Masukkan nilai kedua : "))
        hasil = nilai_pertama * nilai_kedua 
        print("Hasil pengalian antara %.2f dengan %.2f adalah %.2f" % (nilai_pertama, nilai_kedua, hasil))
    elif pilihan == 4:
        nilai_pertama = float(input("Masukkan nilai pertama : "))
        nilai_kedua = float(input("Masukkan nilai kedua : "))
        hasil == nilai_pertama / nilai_kedua
        print("Hasil pembagian antara %.2f dengan %.2f adalah %.2f" % (nilai_pertama, nilai_kedua, hasil))
    elif pilihan == 5:
        print("Terimakasih, telah menggunakan kalkulator", nama)
        break
    else:
        print("Input anda salah, silahkan coba lagi")