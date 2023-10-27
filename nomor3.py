ket = '''Selamat Datang di aplikasi menghitung luas bangun datar
Masukan pilihan :
1 = menghitung luas persegi
2 = menghitung luas lingkaran
3 = menghitung luas segitiga
silahkan pilih ?
'''
pilihan = input (ket)

match pilihan:
    case "1" :
        print ("Pilih 1 untuk menghitung luas persegi")
        sisi = int(input ("masukan sisi ?"))
        LPersegi = sisi * sisi
        print ("luas persegi adalah", LPersegi)
    case "2":
        print("Pilih 2 untuk menghitung luas lingkaran")
        r = int (input ("masukan jari-jari ?"))
        LLingkaran = 3.14 * r**2
        print ("Luas Lingkaran adalah", LLingkaran)
    case "3":
        print ("Pilih 3 untuk menghitung luas segitiga")
        alas = int(input ("masukan alas ?"))
        tinggi = int(input ("masukan tinggi ?"))
        LuasSegitiga = 0.5 * alas * tinggi
        print ("Luas Segitiga", LuasSegitiga)
    case _:
        print ("pilihan  salah")