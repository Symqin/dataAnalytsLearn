# data struktur

# list (Ordered, Mutable Collections)
buah = ["apel", "jeruk", "pisang"]  # list of strings
angka = [1, 2, 3, 4, 5]  # list of integers
campuran = [1, "dua", 3.0, True]

# tuple (Ordered, Immutable Collections)
koordinat = (10.0, 20.0)  # tuple of floats
warna = ("merah", "hijau", "biru")  # tuple of strings
campurat_tuple = (1, "dua", 3.0, False) 

# set (Unordered, Mutable Collections of Unique Elements)
buah_set = {"apel", "jeruk", "pisang"}  # set of strings
angka_set = {1, 2, 3, 4, 5}  # set of integers
campuran_set = {1, "dua", 3.0, True}

# dictionary (Key-Value Pairs)
person = {
    "nama": "John Doe",
    "umur": 30,
    "pekerjaan": "programmer"
}

# file handling
try:
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File tidak ditemukan.")
except IOError:
    print("Terjadi kesalahan saat membaca file.")

"""
"r" → Membaca file
"w" → Menulis file (menghapus isi lama)
"a" → Menambah isi di akhir file
"r+" → Membaca + menulis
"b" → Mode binary (misalnya "rb")
"""

# error handling

try: 
    result = 10 / 0  # ini akan menyebabkan ZeroDivisionError
except ZeroDivisionError:
    print("Tidak bisa membagi dengan nol.")
except Exception as e:
    print("Terjadi kesalahan:", e)
