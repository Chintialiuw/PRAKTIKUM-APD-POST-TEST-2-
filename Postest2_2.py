#Program Data Mahasiswa
def biodata():
    nama = str(input("Masukkan Nama Mahasiwa : "))
    nim = int(input("Masukkan Nomor Induk Mahasiswa : "))
    prodi = str(input("Masukkan Program Studi yang ditempuh : "))
    ipk = float(input("Masukkan Indeks Prestasi Kumulatif terakhir : "))
    ta = int(input("Masukkan Tahun Ajaran [2021, 2005, atau 2089] : "))

def intro():
    print ("=======================================")
    print ("        Program Data Mahasiswa        ")
    print ("=======================================")
intro ()

def menu():
    menu == 1
    while menu != 0:
        print ("\nSilahkan Pilih Menu")
        print ("1. Masukkan Data")
        print ("2. Menampilkan Data")
        print ("3. Keluar dari Program")
        print ("=======================================")

        pilihan = int(input("\nMasukkan Pilihan Menu Anda (1, 2 atau 3) : "))
        if pilihan == 1:
            biodata()
        elif pilihan == 2:
            list_biodata = ["Bambang Susanto", "1210206008", "Informatika", "3.98", "2012"]
            print ("Nama Mahasiswa : ",list_biodata[0])
            print ("Nomor Induk Mahasiswa : ",list_biodata[1])
            print ("Program Studi yang Ditempuh : ",list_biodata[2])
            print ("Indeks Prestasi Kumulatif Terakhir : ",list_biodata[3])
            print ("Tahun Ajaran : ",list_biodata[4])
            print ("=======================================")
            print ([list_biodata[0], list_biodata[1], list_biodata[2], list_biodata[3], list_biodata[4]])
        elif pilihan == 3:
            yakin = str(input("Apakah Anda Yakin untuk keluar dari program [y/t] ? "))
            print ("=======================================")
            if yakin == "y":
                print ("Terima Kasih")
                exit()
            elif yakin == "t":
                menu()
        else:
            print ("Maaf Pilihan yang Anda Masukkan Salah, Silahkan Coba lagi")

        jawab = str(input("\nApakah Anda ingin Kembali ke Menu [y/t] ? "))
        print ("=======================================")
        if jawab == "y" :
            menu()
        elif jawab == "t":
            print ("Terima Kasih")
            exit()
menu()