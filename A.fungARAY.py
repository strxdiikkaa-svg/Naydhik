def hitung_total(daftar_harga):
    total = 0
    for harga in daftar_harga:
        total += harga
    return total

belanjaan = [15000, 25000, 10000]
print("total belanja:", hitung_total(belanjaan))
