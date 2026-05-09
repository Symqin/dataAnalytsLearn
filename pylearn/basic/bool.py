# Boolean

# --- CASE 1: Deklarasi Nilai Boolean Langsung ---
is_light_on = True
is_door_locked = False

print(is_light_on)     # Output: True
print(is_door_locked)  # Output: False

# --- CASE 2: Boolean dari Operasi Perbandingan ---
x = 5
y = 10

print(x == y)  # Output: False
print(x < y)   # Output: True

# --- CASE 3: Operasi Logika (and, or, not) ---
a = True
b = False

print(a and b)  # Output: False
print(a or b)   # Output: True
print(not a)    # Output: False

# --- CASE 4: Boolean dalam Percabangan (If-Else Dasar) ---
temperature = 30

if temperature > 25:
    print("Hari ini panas!")
else:
    print("Hari ini tidak terlalu panas.")

# --- CASE 5: Boolean dalam Percabangan Kondisi (If-Elif-Else) ---
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Nilai Anda adalah {grade}.")

# --- CASE 6: Boolean dalam Percabangan Bersarang (Nested If) ---
age = 20
has_license = True

if age >= 18:
    if has_license:
        print("Anda memenuhi syarat untuk mengemudi.")
    else:
        print("Anda perlu memiliki SIM untuk mengemudi.")
else:
    print("Anda terlalu muda untuk mengemudi.")

# --- CASE 7: Aplikasi Praktis - Menentukan Bilangan Genap atau Ganjil ---
number = 7

if number % 2 == 0:
    print(f"{number} adalah bilangan genap.")
else:
    print(f"{number} adalah bilangan ganjil.")

# --- CASE 8: Aplikasi Praktis - Validasi Input Pengguna ---
# Catatan: Jika tidak ingin memblokir program, input dapat diisi langsung, contoh: user_input = "25"
user_input = input("Masukkan angka positif: ")

if user_input.isdigit():
    number_input = int(user_input)
    if number_input > 0:
        print(f"Anda memasukkan angka positif yang valid: {number_input}")
    else:
        print("Angka harus lebih besar dari nol.")
else:
    print("Input tidak valid. Masukkan angka numerik.")

# --- CASE 9: Aplikasi Praktis - Sistem Penilaian ---
score2 = 78

if score2 >= 90:
    grade = "A"
    feedback = "Kerja luar biasa!"
elif score2 >= 80:
    grade = "B"
    feedback = "Bagus sekali!"
elif score2 >= 70:
    grade = "C"
    feedback = "Tetap tingkatkan."
else:
    grade = "F"
    feedback = "Anda perlu belajar lebih keras."

print(f"Nilai: {grade}\nUmpan Balik: {feedback}")


# --- KESALAHAN UMUM & PRAKTIK TERBAIK ---

# --- CASE 10: Kesalahan Umum (Menggunakan = vs ==) ---
# SALAH: if x = 5: -> akan menghasilkan Error karena '=' berarti assignment (pemberian nilai).
# BENAR: Menggunakan '==' untuk perbandingan.
test_x = 5
if test_x == 5:
    print("test_x adalah 5")

# --- CASE 11: Kesalahan Umum (Kondisi Terlalu Rumit) ---
# Lebih baik memisahkan kondisi agar lebih mudah dibaca daripada menulisnya dalam satu baris panjang
test_y = 35

in_range_x = 10 < test_x < 20
in_range_y = 30 < test_y < 40

if in_range_x or in_range_y:
    print("Kondisi terpenuhi dengan penulisan yang lebih bersih.")

# --- CASE 12: Praktik Terbaik (Gunakan Nama Variabel yang Deskriptif) ---
# Menggunakan variabel yang mendeskripsikan tujuan kondisinya
min_value = 5
max_value = 10

if min_value < max_value:
    print("Kondisi menggunakan variabel deskriptif benar.")


#