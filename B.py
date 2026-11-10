def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: Tidak bisa dibagi 0"
    return a / b

def tampilkan_menu():
    print("\n===== KALKULATOR =====")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Keluar")

# ======================
# PROGRAM UTAMA
# ======================
while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "5":
        print("Terima kasih, program selesai.")
        break

    if pilihan not in ["1", "2", "3", "4"]:
        print("Pilihan tidak valid!")
        continue

    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    if pilihan == "1":
        hasil = tambah(angka1, angka2)
        print("Hasil:", hasil)
    elif pilihan == "2":
        hasil = kurang(angka1, angka2)
        print("Hasil:", hasil)
    elif pilihan == "3":
        hasil = kali(angka1, angka2)
        print("Hasil:", hasil)
    elif pilihan == "4":
        hasil = bagi(angka1, angka2)
        print("Hasil:", hasil)