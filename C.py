#==================================
# Kartu menghafal materi pelajaran 
#==================================

import random

flashcard = []

def tambah_kartu():
    print("\n--- Tambah Flashcard Baru ---")
    pelajaran = input("Mata Pelajaran: ").strip()
    pertanyaan = input("Pertanyaan: ").strip()
    jawaban = input("Jawaban: ").strip()

    if pertanyaan and jawaban:
        kartu = {
            "pelajaran": pelajaran,
            "pertanyaan": pertanyaan,
            "jawaban": jawaban
        }
        flashcard.append(kartu)
        print("Flashcard berhasil ditambahkan!")
    else:
        print("Pertanyaan dan jawaban tidak boleh kosong.")

def lihat_semua_kartu():
    if not flashcard:
        print("\nBelum ada flashcard yang dibuat.")
        return

    print("\n======== Daftar Flashcard ========")
    for i, kartu in enumerate(flashcard, 1):
        print(f"{i}. [{kartu['pelajaran']}]")
        print(f"   Q: {kartu['pertanyaan']}")
        print(f"   A: {kartu['jawaban']}")
        print("-" * 40)
    print("==================================")

def latihan():
    if not flashcard:
        print("\nBelum ada flashcard. Silakan tambah dulu.")
        return

    print("\n================== MODE LATIHAN ==================")
    print("Ketik jawabanmu, atau ketik 'keluar' untuk berhenti.\n")

    kartu_latihan = flashcard.copy()
    random.shuffle(kartu_latihan)

    benar = 0
    total = 0

    for kartu in kartu_latihan:
        print(f"Pelajaran : {kartu['pelajaran']}")
        print(f"Pertanyaan: {kartu['pertanyaan']}")

        jawaban_user = input("Jawaban kamu: ").strip()

        if jawaban_user.lower() == "keluar":
            break

        total += 1
        if jawaban_user.lower() == kartu['jawaban'].lower():
            print("Benar!\n")
            benar += 1
        else:
            print(f"Salah. Jawaban yang benar: {kartu['jawaban']}\n")

    if total > 0:
        print(f"Hasil latihan: {benar}/{total} benar")
        print("==================================================")

def main():
    print("=" * 45)
    print("       FlashCard Pintar")
    print("   Belajar materi lebih mudah")
    print("=" * 45)

    while True:
        print("\nMenu:")
        print("1. Tambah FlashCard")
        print("2. Lihat Semua FlashCard")
        print("3. Mulai Latihan")
        print("4. Keluar")

        pilihan = input("\nPilih menu (1-4): ").strip()

        if pilihan == "1":
            tambah_kartu()
        elif pilihan == "2":
            lihat_semua_kartu()
        elif pilihan == "3":
            latihan()
        elif pilihan == "4":
            print("\nSemangat belajarnya!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()