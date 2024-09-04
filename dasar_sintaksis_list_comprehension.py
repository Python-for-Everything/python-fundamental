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

print('\nMembuat list baru')
daftar_buku = ['Seven Habits','How to Influence People','First Things Frist','4DX']
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list new')
del daftar_buku[:]
for i in range(0,len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension (genap)')
daftar_buku = ['1 Seven Habits','2 How to Influence People','3 First Things Frist','4 4DX']
daftar_buku_baru = daftar_buku[1::2] #start stop end
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension (ganjil)')
daftar_buku = ['1 Seven Habits','2 How to Influence People','3 First Things Frist','4 4DX']
daftar_buku_baru = daftar_buku[1::3] #stat stop end
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension custom (- minus 1 || buang di ujung)')
daftar_buku = ['1 Seven Habits','2 How to Influence People','3 First Things Frist','4 4DX']
daftar_buku_baru = daftar_buku[0:-1]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension custom (0:-1:2')
daftar_buku = ['1 Seven Habits','2 How to Influence People','3 First Things Frist','4 4DX']
daftar_buku_baru = daftar_buku[0:-1:2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension (ganjil)')
daftar_buku = ['1 Seven Habits','2 How to Influence People','3 First Things Frist','4 4DX']
print(daftar_buku[0::2])
