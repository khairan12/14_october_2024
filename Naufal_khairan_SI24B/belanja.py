total_belanja = float(input("masukkan total belanja: "))

if total_belanja >= 500000:
    diskon = 0.20  # 20%
elif total_belanja >= 250000:
    diskon = 0.15  # 15%
elif total_belanja >= 100000:
    diskon = 0.10  # 10%
else:
    diskon = 0.0  # Tidak ada diskon

jumlah_diskon = total_belanja * diskon
total_setelah_diskon = total_belanja - jumlah_diskon

print(f"diskon: {diskon * 100}%")
print(f"total setelah diskon: {total_setelah_diskon}")