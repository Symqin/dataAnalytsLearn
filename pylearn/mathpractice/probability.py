# probability

# simulasi pelemparan dadu

import numpy as np

# Simulasi pelemparan dadu sebanyak 10000 kali
np.random.seed(0)  # Untuk memastikan hasil yang sama setiap kali dijalankan
throws = np.random.randint(1, 7, size=10000) # Menghasilkan angka antara 1 dan 6
even_count = np.sum(throws % 2 == 0) # Menghitung jumlah angka genap
probability_even = even_count / len(throws) # Menghitung probabilitas angka genap
print(f"Probabilitas mendapatkan angka genap: {probability_even:.4f}")

# probabillitas bersyarat
# Simulasi pelemparan tiga dadu sebanyak 10000 kali
throws = np.random.randint(1, 7, size=(10000, 3)) # Menghasilkan angka antara 1 dan 6 untuk tiga dadu
# Menghitung jumlah pelemparan di mana dadu pertama menunjukkan angka 6 dan dadu kedua menunjukkan angka 5
condition_count = np.sum((throws[:, 0] == 6) & (throws[:, 1] == 5))
# Menghitung jumlah pelemparan di mana dadu pertama menunjukkan angka 6
first_die_count = np.sum(throws[:, 0] == 6)
# Menghitung probabilitas bersyarat
conditional_probability = condition_count / first_die_count if first_die_count > 0 else 0
print(f"Probabilitas mendapatkan angka 5 pada dadu kedua, given angka 6 pada dadu pertama: {conditional_probability:.4f}")