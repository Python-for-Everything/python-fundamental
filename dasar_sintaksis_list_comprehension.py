print('\nPerintah Del dengan list comprehension')
daftar_buku = ['Seven Habits','How to Influence People','First Things Frist','4DX']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah Del dengan list comprehension start // tidak ada yang dihapus')
daftar_buku = ['Seven Habits','How to Influence People','First Things Frist','4DX']
del daftar_buku[0:0] #START:END
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah Del dengan list comprehension start stop with step')
daftar_buku = ['Seven Habits','How to Influence People','First Things Frist','4DX']
del daftar_buku[0::2] #START:END:STEP
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])