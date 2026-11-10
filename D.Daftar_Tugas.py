daftar_tugas = []

#menambahkan tugass

def tambah_tugas():
    nama = input("Nama tugas: ").strip

    if not nama:
        print("Nama tugas tidak boleh kosong")
        return
    tugas = {
        "nama": nama,
        "selesai": False
    }
    daftar_tugas.append(tugas)
    print("Tugas berhasil Ditambahkan")

def lihat_tugas():
    if not daftar_tugas:
        print("Belum ada tugas")
        return
    for nomor, tugas in enumerate(daftar_tugas, start=1):
        status = "selesai" if tugas["selesai"] else "Belum selesai"
        print(f"{nomor}. {tugas['nama']} - {status}")

def selesaikan_tugas():
    lihat_tugas()
    if not daftar_tugas:
        return
    try:
        nomor = int(input("Nomomr tugas yang selesai"))
    except ValueError:
        print("Masukkan nomer berupa angka tugas")
        return
    if 1 <= nomor <=len(daftar_tugas):
        daftar_tugas[nomor - 1]["selesai"] = True
        print("Tugas ditandai Selesai")
    else:
        print("Nomor tugas tidak ditemukan")

def main():
    #MENU UTAMA APK
    while True:
        print("\n======STUDYMATE======")
        print("1. Tambahkan tugas")
        print("2. Lihat tugas")
        print("3. Selesaiakan tugas")
        print("4. Keluar")

        pilihan = input("Pilih menu: ").strip

        if pilihan == "1":
            tambah_tugas()
        elif pilihan == "2":
            lihat_tugas()
        elif pilihan == "3":
            selesaikan_tugas()
        elif pilihan == "4":
            print("Terimakasih")
            break
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()