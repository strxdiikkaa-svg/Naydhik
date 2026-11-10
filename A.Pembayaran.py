# Sistem Kasir Sederhana

keranjang = []

def tambah_barang():
    print("\n--- Tambah Barang ---")
    nama = input("Nama barang: ").strip()

    if not nama:
        print("Nama barang tidak boleh kosong!")
        return

    try:
        harga = int(input("Harga Satuan: "))
        jumlah = int(input("Jumlah: "))
    except ValueError:
        print("Harga dan jumlah harus berupa angka!")
        return

    if harga <= 0 or jumlah <= 0:
        print("Harga dan jumlah harus lebih dari 0!")
        return

    barang = {
        "nama": nama,
        "harga": harga,
        "jumlah": jumlah,
        "subtotal": harga * jumlah
    }
    keranjang.append(barang)
    print(f"'{nama}' berhasil ditambahkan ke keranjang.")


def lihat_keranjang():
    if not keranjang:
        print("\nKeranjang masih kosong.")
        return

    print("\n========== KERANJANG BELANJA ==========")
    total = 0
    for i, barang in enumerate(keranjang, 1):
        print(f"{i}. {barang['nama']} x{barang['jumlah']} = Rp{barang['subtotal']:,}")
        total += barang['subtotal']

    print("-" * 40)
    print(f"Total Belanja : Rp{total:,}")
    print("=======================================")


def bayar():
    if not keranjang:
        print("\nKeranjang masih kosong. Tidak bisa bayar.")
        return

    total = sum(barang['subtotal'] for barang in keranjang)

    diskon = 0
    if total >= 50000:
        diskon = int(total * 0.10)  # Diskon 10%
        print(f"\nSelamat! Anda mendapat diskon 10% = Rp{diskon:,}")

    total_bayar = total - diskon

    print("\n========== RINCIAN PEMBAYARAN ==========")
    print(f"Total Belanja : Rp{total:,}")
    print(f"Diskon        : Rp{diskon:,}")
    print(f"Total Bayar   : Rp{total_bayar:,}")
    print("========================================")

    try:
        uang = int(input("\nMasukkan uang pembayaran: Rp"))
    except ValueError:
        print("Input harus berupa angka!")
        return

    if uang < total_bayar:
        print("Uang tidak cukup!")
    else:
        kembalian = uang - total_bayar
        print(f"\nPembayaran berhasil!")
        print(f"Kembalian     : Rp{kembalian:,}")
        print("Terima kasih telah berbelanja!")
        keranjang.clear()


def main():
    print("=" * 45)
    print("       SISTEM KASIR SEDERHANA")
    print("=" * 45)

    while True:
        print("\nMenu:")
        print("1. Tambah Barang")
        print("2. Lihat Keranjang")
        print("3. Bayar")
        print("4. Keluar")

        pilihan = input("\nPilih Menu (1-4): ").strip()

        if pilihan == "1":
            tambah_barang()
        elif pilihan == "2":
            lihat_keranjang()
        elif pilihan == "3":
            bayar()
        elif pilihan == "4":
            print("\nTerima kasih, sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()