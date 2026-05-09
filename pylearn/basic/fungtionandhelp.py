# Function and Help

# cara mendefinisikan fungsi
def nama_fungsi(parameter):
    """Docstring yang menjelaskan fungsi."""
    # Tubuh fungsi
    return hasil

def tambah_angka(a, b):
    """Mengembalikan jumlah dua angka."""
    return a + b

# menggunakan fungsi
hasil = tambah_angka(5, 3)
print(hasil)  # Output: 8

# mengembalikan nilai fungsi

def hitung_luas_persegi(sisi):
    """Menghitung luas persegi dengan sisi tertentu."""
    return sisi * sisi

luas = hitung_luas_persegi(4)
print(luas)  # Output: 16

# fungsi bawaan Python
print("Hello, World!")  # Output: Hello, World!
len("Python")  # Output: 6
type(42)  # Output: <class 'int'>
sum([1, 2, 3, 4])  # Output: 10

# help() untuk melihat dokumentasi fungsi
help(print)  # Menampilkan dokumentasi fungsi print
help(len)  # Menampilkan dokumentasi fungsi len

def kalikan(a, b):
    """Mengalikan dua angka dan mengembalikan hasilnya."""
    return a * b

help(kalikan)


# mengakses dokstrings
print(kalikan.__doc__)  # Output: Mengalikan dua angka dan mengembalikan hasilnya.


# default args
def greet(name="Guest"):
    """Mengembalikan salam dengan nama yang diberikan."""
    return f"Hello, {name}!"
print(greet())  # Output: Hello, Guest!
print(greet("Alice"))  # Output: Hello, Alice!

# argumen panjang

def sum_all(*args):
    """Mengembalikan jumlah dari semua argumen yang diberikan."""
    return sum(args)   

print(sum_all(1, 2, 3))  # Output: 6
print(sum_all(4, 5))     # Output: 9

#lambda function

square = lambda x: x ** 2
print(square(5))  # Output: 25  


#test

def is_even(number):
    """Checks if a number is even."""
    return number % 2 == 0

# Test cases
print(is_even(4))  # Output: True
print(is_even(7))  # Output: False