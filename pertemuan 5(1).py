#NO 1
#point a
kendaraan = ['honda beat', 'sepeda motor', 120, 'merah', 2]
print(kendaraan)


#point b

kendaraan.append(20000000)
kendaraan.append('matic')
print(kendaraan)

kendaraan.extend([20000000, 'matic'])
print(kendaraan)

#point c
kendaraan.insert(2, 'honda beat')
print(kendaraan)

#NO 2

print('ini adalah program sederhana untuk menghitung luas bangun datar')
print("pilih menu angka 1-3 : /n1. persegi/n2. lingkaran/n3. segitiga")
pilihmenu = int(input("silahkan pilih menu dengan mengetikan angka 1-3 : "))

match pilihmenu:
    case 1:
        print("ini adalah menu untuk menghitung luas persegi")
        sisi = int(input("silahkan masukan nilai yang mau dihitung"))
        hitung = sisi*sisi
        print(f"luas persegi adalah: {hitung}")

    case 2:
        print("ini adalah menu untuk menghitung luas lingkaran")
        jari_jari = float(input("Masukkan jari-jari lingkaran: "))
        luas = jari_jari**2
        print("luas lingkaran adalah:", luas)

    case 3:
        print("ini adalah menu untuk menghitung luas segitiga")
        alas = float(input("Masukkan panjang alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        luas = 0.5 * alas * tinggi
        print(luas)
    case _:
        print("pilihan tidak valid, silahkan pilih antara 1-3")