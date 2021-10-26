#Program Konversi Suhu
def suhu0():
    suhu0 = int(input("Masukkan suhu : "))
    hitung0 = float(suhu0 - 32) * 5 / 9
    print ("Hasil Konversi Suhu dari Fahrenheit ke Celcius adalah : ", hitung0)

def suhu1():
    suhu1 = int(input("Masukkan suhu : "))
    hitung1 = int(suhu1 - 273)
    print ("Hasil Konversi Suhu dari Kelvin ke Celcius adalah : ", hitung1)

def suhu2():
    suhu2 = int(input("Masukkan suhu : "))
    hitung2 = float(suhu2 * 5 / 4)
    print ("Hasil Konversi Suhu dari Reamour ke Celcius adalah : ", hitung2)

def intro():
    print ("=======================================")
    print ("   Program Konversi Suhu ke Celcius   ")
    print ("=======================================")
intro ()

def menu():
    pilihan = "a"
    while  pilihan != "d":
        print ("\nSilahkan Pilih Menu")
        print ("a. Konversi Suhu dari Fahrenheit ke Celcius")
        print ("b. Konversi Suhu dari Kelvin ke Celcius")
        print ("c. Konversi Suhu dari Reamour ke Celcius")
        print ("d. Keluar dari Program")
        print ("=======================================")
  
        pilihan = str(input("\nMasukkan Pilihan Menu Anda [a, b, c atau d] : "))
        if pilihan == "a":
            print ("Masukkan Angkanya Saja !")
            suhu0()
        elif pilihan == "b":
            print ("Masukkan Angkanya Saja !")
            suhu1()
        elif pilihan == "c":
            print ("Masukkan Angkanya Saja !")
            suhu2()
        elif pilihan == "d":
            yakin = str(input("Apakah Anda Yakin untuk keluar dari program [y/t] ? "))
            print ("=======================================")
            if yakin == "y":
                print ("Terima Kasih")
                exit()
            elif yakin == "t":
                menu()
        else:
            print ("Maaf Pilihan yang Anda Masukkan Salah, Silahkan Coba lagi")

        jawab = str(input("\nApakah Anda ingin Menghitung Kembali [y/t] ? "))
        print ("=======================================")
        if jawab == "y" :
            menu()
        elif jawab == "t":
            print ("Terima Kasih")
            exit()
menu()   