"""
Program Perulangan Membaca Buku dengan While sampai Paham
"""
book_count = 10 # 10.5 --> bilangan asli
print('Ibu berkata, "Baca semua bukumu"')
read_count = 0

understood_count = 0
print(f'Jumlah buku yang sudah dibaca dan dipahami {understood_count}')

# with while
while read_count < book_count * 2:
    read_count = read_count + 1
    if understood_count == 9:
        print(f"Buku ke {understood_count + 1} belum paham")
    else:
        understood_count = understood_count + 1
        print(f"Buku ke {understood_count} sudah dibaca dan dipahami")

print(f'jumlah buku yang sudah dibaca dan dipahami {understood_count}')
if understood_count == book_count:
    print('"Bu, semua buku sudah dibaca dan dipahami')
else:
    print(f'"Bu, tidak semua buku bisa dipahami. '
          f' Budi hanya bisa memahami" {understood_count} buku')



