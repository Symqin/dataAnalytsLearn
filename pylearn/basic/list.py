# LIST 

buah = ['apel', 'jeruk', 'mangga', 'pisang']
print(buah[0]) # Output: apel
print(buah[1]) # Output: jeruk

for item in buah:
    print(item)

for index, b in enumerate(buah):
    print(f"Index: {index}, Buah: {b}")

campuran = [1, 'dua', 3.0, True]
print(campuran[0]) # Output: 1
print(campuran[-1]) # Output: True

listkosong = []
print(listkosong) # Output: []

# Mengubah elemen dalam list
buah[1] = 'anggur'
print(buah) # Output: ['apel', 'anggur', 'mangga', 'pisang']
# Menambahkan elemen ke dalam list
buah.append('kiwi')
print(buah) # Output: ['apel', 'anggur', 'mangga', 'pisang', 'kiwi']
# Menghapus elemen dari list
buah.remove('mangga')
print(buah) # Output: ['apel', 'anggur', 'pisang', 'kiwi']
# Menyisipkan elemen ke dalam list
buah.insert(1, 'melon')
print(buah) # Output: ['apel', 'melon', 'anggur', 'pisang', 'kiwi']
#menabahkan banyak elemen ke dalam list
buah.extend(['nanas', 'semangka']) 
print(buah) # Output: ['apel', 'melon', 'anggur', 'pisang', 'kiwi', 'nanas', 'semangka']
#menghapus elemen pada index tertentu dan mengembalikan nilai yang dihapus
dihapus = buah.pop(2)
print(dihapus) # Output: 'anggur'
print(buah) # Output: ['apel', 'melon', 'pisang', 'kiwi', 'nanas', 'semangka']
# Menghapus elemen atau irisan tertentu menggunakan del
del buah[0]
print(buah) # Output: ['melon', 'pisang', 'kiwi', 'nanas', 'semangka']


# list comprehension

angka = [1, 2, 3, 4, 5]
kuadrat = [x ** 2 for x in angka]
print(kuadrat) # Output: [1, 4, 9, 16, 25]

genap = [x for x in angka if x % 2 == 0]
print(genap) # Output: [2, 4]


# loop dengan list comprehension
matriks = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rata = []
for baris in matriks:
    for elemen in baris:
        rata.append(elemen)
print(rata) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]