"""Pengingat Tugas Sekolah (CLI)

Program untuk mencatat, melihat, menandai selesai, dan menghapus tugas sekolah.
Ditambah fitur Absensi Virtual.
"""

import json
from datetime import datetime

NAMA_FILE = "tugas.json"
FILE_ABSENSI = "absensi.json"
FORMAT_TANGGAL = "%Y-%m-%d"  # contoh input: 2026-11-05


def muat_data():
    """Baca daftar tugas dari NAMA_FILE dan kembalikan sebagai list."""
    try:
        with open(NAMA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def simpan_data(daftar_tugas):
    """Simpan list tugas ke NAMA_FILE dalam format JSON."""
    with open(NAMA_FILE, "w", encoding="utf-8") as f:
        json.dump(daftar_tugas, f, indent=4, ensure_ascii=False)


def muat_absensi():
    """Baca data absensi dari FILE_ABSENSI."""
    try:
        with open(FILE_ABSENSI, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def simpan_absensi(daftar_absensi):
    """Simpan data absensi ke FILE_ABSENSI."""
    with open(FILE_ABSENSI, "w", encoding="utf-8") as f:
        json.dump(daftar_absensi, f, indent=4, ensure_ascii=False)


def tambah_tugas(daftar_tugas):
    """Minta input mapel, judul, dan tenggat, lalu tambahkan ke daftar."""
    print("\n--- Tambah Tugas Baru ---")
    mapel = input("Mata pelajaran: ").strip()
    judul = input("Judul tugas  : ").strip()

    while True:
        tenggat = input("Tenggat (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(tenggat, FORMAT_TANGGAL)
            break
        except ValueError:
            print("Format tanggal salah! Contoh yang benar: 2026-11-05")

    tugas_baru = {
        "mapel": mapel,
        "judul": judul,
        "tenggat": tenggat,
        "selesai": False
    }
    daftar_tugas.append(tugas_baru)
    simpan_data(daftar_tugas)
    print("Tugas berhasil ditambahkan!")


def hitung_sisa_hari(tenggat):
    """Kembalikan selisih hari antara hari ini dan tenggat (bilangan bulat)."""
    tanggal_tenggat = datetime.strptime(tenggat, FORMAT_TANGGAL).date()
    hari_ini = datetime.now().date()
    return (tanggal_tenggat - hari_ini).days


def tampilkan_tugas(daftar_tugas):
    """Tampilkan semua tugas, urut dari tenggat terdekat."""
    if not daftar_tugas:
        print("\nBelum ada tugas.")
        return

    daftar_urut = sorted(daftar_tugas, key=lambda x: x["tenggat"])

    print("\n===== DAFTAR TUGAS =====")
    for i, tugas in enumerate(daftar_urut, start=1):
        sisa = hitung_sisa_hari(tugas["tenggat"])

        if tugas["selesai"]:
            status = "SELESAI"
        elif sisa < 0:
            status = "TERLAMBAT"
        elif sisa <= 2:
            status = "SEGERA"
        else:
            status = "AMAN"

        print(f"{i}. [{status}] {tugas['mapel']} - {tugas['judul']}")
        print(f"   Tenggat: {tugas['tenggat']} (sisa {sisa} hari)")
    print("========================")


def tandai_selesai(daftar_tugas):
    """Pilih nomor tugas, ubah 'selesai' menjadi True."""
    if not daftar_tugas:
        print("\nBelum ada tugas.")
        return

    tampilkan_tugas(daftar_tugas)

    try:
        nomor = int(input("\nMasukkan nomor tugas yang selesai: "))
        if 1 <= nomor <= len(daftar_tugas):
            daftar_urut = sorted(daftar_tugas, key=lambda x: x["tenggat"])
            tugas_dipilih = daftar_urut[nomor - 1]

            for tugas in daftar_tugas:
                if (tugas["mapel"] == tugas_dipilih["mapel"] and
                    tugas["judul"] == tugas_dipilih["judul"] and
                    tugas["tenggat"] == tugas_dipilih["tenggat"]):
                    tugas["selesai"] = True
                    break

            simpan_data(daftar_tugas)
            print("Tugas berhasil ditandai selesai!")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Masukkan angka yang benar.")


def hapus_tugas(daftar_tugas):
    """Pilih nomor tugas, hapus dari daftar."""
    if not daftar_tugas:
        print("\nBelum ada tugas.")
        return

    tampilkan_tugas(daftar_tugas)

    try:
        nomor = int(input("\nMasukkan nomor tugas yang ingin dihapus: "))
        if 1 <= nomor <= len(daftar_tugas):
            daftar_urut = sorted(daftar_tugas, key=lambda x: x["tenggat"])
            tugas_dipilih = daftar_urut[nomor - 1]

            konfirmasi = input(f"Yakin hapus '{tugas_dipilih['judul']}'? (y/n): ").lower()
            if konfirmasi == "y":
                daftar_tugas.remove(tugas_dipilih)
                simpan_data(daftar_tugas)
                print("Tugas berhasil dihapus!")
            else:
                print("Penghapusan dibatalkan.")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Masukkan angka yang benar.")


def tampilkan_statistik(daftar_tugas):
    """Tampilkan jumlah tugas total, selesai, belum selesai, dan terlambat."""
    total = len(daftar_tugas)
    selesai = sum(1 for t in daftar_tugas if t["selesai"])
    belum = total - selesai
    terlambat = sum(1 for t in daftar_tugas if not t["selesai"] and hitung_sisa_hari(t["tenggat"]) < 0)

    print("\n===== STATISTIK TUGAS =====")
    print(f"Total tugas     : {total}")
    print(f"Selesai         : {selesai}")
    print(f"Belum selesai   : {belum}")
    print(f"Terlambat       : {terlambat}")
    print("===========================")


def absensi_virtual():
    """Fitur Absensi Virtual sesuai alur yang diminta."""
    print("\n===== ABSENSI VIRTUAL =====")

    # 1. Tanggal hari ini
    while True:
        tanggal = input("1. Masukkan tanggal hari ini (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(tanggal, FORMAT_TANGGAL)
            break
        except ValueError:
            print("Format tanggal salah! Contoh: 2026-10-21")

    # 2. Nama
    nama = input("2. Masukkan nama anda: ").strip()
    if not nama:
        print("Nama tidak boleh kosong! Absensi gagal.")
        return

    # 3. Absen
    absen = input("3. Masukkan absen anda (Hadir/Izin/Sakit): ").strip().capitalize()
    if absen not in ["Hadir", "Izin", "Sakit"]:
        print("Pilihan absen harus Hadir / Izin / Sakit. Absensi gagal.")
        return

    # 4. Keadaan
    while True:
        keadaan = input("4. Keadaan anda (sehat/sakit): ").strip().lower()
        if keadaan in ["sehat", "sakit"]:
            break
        print("Masukkan 'sehat' atau 'sakit' saja.")

    # 5. Ada tugas hari ini?
    while True:
        ada_tugas = input("5. Apakah ada tugas hari ini (ya/tidak): ").strip().lower()
        if ada_tugas in ["ya", "tidak"]:
            break
        print("Masukkan 'ya' atau 'tidak' saja.")

    mapel_hari_ini = ""
    status_tugas = ""

    if ada_tugas == "ya":
        # 6. Tugas / mapel hari ini
        mapel_hari_ini = input("6. Apa tugas/mapel hari ini yang ada: ").strip()
        if not mapel_hari_ini:
            print("Tugas/mapel tidak boleh kosong! Absensi gagal.")
            return

        # 7. Apakah tugas sudah selesai?
        while True:
            sudah_selesai = input("7. Apakah tugas anda sudah selesai (ya/tidak): ").strip().lower()
            if sudah_selesai in ["ya", "tidak"]:
                break
            print("Masukkan 'ya' atau 'tidak' saja.")

        if sudah_selesai == "ya":
            print("\n>>> Selamat! Tugas sudah selesai. Kamu bisa bersantai. <<<")
            status_tugas = "Selesai"
        else:
            print("\n>>> Semangat mengerjakan tugasnya ya! Jangan menyerah! <<<")
            status_tugas = "Belum selesai"
    else:
        print("\nTidak ada tugas hari ini. Santai saja!")
        status_tugas = "Tidak ada tugas"

    # 8. Absensi diterima
    print("\n----- RINGKASAN ABSENSI -----")
    print(f"Tanggal     : {tanggal}")
    print(f"Nama        : {nama}")
    print(f"Absen       : {absen}")
    print(f"Keadaan     : {keadaan.capitalize()}")
    print(f"Ada tugas   : {ada_tugas.capitalize()}")
    if ada_tugas == "ya":
        print(f"Mapel/Tugas : {mapel_hari_ini}")
        print(f"Status tugas: {status_tugas}")
    print("-----------------------------")
    print(">>> Absensi DITERIMA dan LENGKAP! <<<")

    # 9. Ucapan selamat
    print("\nSelamat! Absensi berhasil.")
    print("Jangan lupa jaga kesehatan ya! 💪")

    # Simpan ke file
    data_absen = {
        "tanggal": tanggal,
        "nama": nama,
        "absen": absen,
        "keadaan": keadaan,
        "ada_tugas": ada_tugas,
        "mapel_hari_ini": mapel_hari_ini,
        "status_tugas": status_tugas,
        "waktu_input": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    daftar_absensi = muat_absensi()
    daftar_absensi.append(data_absen)
    simpan_absensi(daftar_absensi)
    print("(Data absensi berhasil disimpan)")


def tampilkan_menu():
    print("\n=== PENGINGAT TUGAS SEKOLAH ===")
    print("1. Tambah tugas")
    print("2. Lihat tugas")
    print("3. Tandai selesai")
    print("4. Hapus tugas")
    print("5. Absensi Virtual")
    print("6. Statistik")
    print("0. Keluar")


def main():
    daftar_tugas = muat_data()

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tambah_tugas(daftar_tugas)
        elif pilihan == "2":
            tampilkan_tugas(daftar_tugas)
        elif pilihan == "3":
            tandai_selesai(daftar_tugas)
        elif pilihan == "4":
            hapus_tugas(daftar_tugas)
        elif pilihan == "5":
            absensi_virtual()
        elif pilihan == "6":
            tampilkan_statistik(daftar_tugas)
        elif pilihan == "0":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")


if __name__ == "__main__":
    main()