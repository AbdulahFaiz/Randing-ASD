# Fungsi merge sort

import os
os.system("cls")

daftar = [12, 1, [22, 3, [8, 14]], 2, 6, [11], 90]

def urai(daftar):
    if isinstance(daftar, list):
        hasil = []
        for a in daftar:
            hasil.extend(urai(a))
        return hasil
    else:
        return [daftar]

def merge_sort(daftar):
    if len(daftar) <= 1:
        return daftar
    tengah = len(daftar) // 2
    kiri = daftar[:tengah]
    kanan = daftar[tengah:]
    kiri = merge_sort(kiri)
    kanan = merge_sort(kanan)
    return merge(kiri, kanan)

def merge(kiri, kanan):
    hasil = []
    while kiri and kanan:
        if kiri[0] < kanan[0]:
            hasil.append(kiri.pop(0))
        else:
          hasil.append(kanan.pop(0))
    if kiri:
      hasil += kiri
    elif kanan:
      hasil += kanan
    return hasil

baru = urai(daftar)
p = merge_sort(baru)

print("Hasil Sebelum di Uraikan")
print(daftar)
print("")
print("Hasil Setelah di Uraikan")
print(p)