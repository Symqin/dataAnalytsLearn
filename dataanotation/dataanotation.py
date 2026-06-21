import pandas as pd

# ==========================================
# 1. MEMBUAT DATASET BARU (Dataset Ulasan)
# ==========================================
data = {
    'ID_Ulasan': ['U01', 'U02', 'U03', 'U04', 'U05', 'U06'],
    'Teks_Ulasan': [
        'Kualitas produk sangat bagus dan awet!',
        'Pengiriman sangat lambat, barang sampai cacat.',
        'Kualitas standar, sesuai dengan harganya.',
        'Sangat memuaskan, pasti beli lagi!',
        'Pelanggan kecewa, admin tidak responsif.',
        'Lumayan lah buat dipakai sehari-hari.'
    ],
    'Skor_Rating': [5, 1, 3, 4, 2, 3] # Rating menggunakan skala 1 - 5
}

df_ulasan = pd.DataFrame(data)

print("--- DATASET SEBELUM PELABELAN ---")
print(df_ulasan[['ID_Ulasan', 'Skor_Rating']])


# ==========================================
# 2. PROSES DATA ANNOTATION BERDASARKAN SOP
# ==========================================
# Membuat mapping (kamus) label sesuai dengan SOP Sentimen yang disepakati
sop_mapping = {
    1: 'Negatif',
    2: 'Negatif',
    3: 'Netral',
    4: 'Positif',
    5: 'Positif'
}

# Membuat kolom baru 'Label_Sentimen' dengan mengaplikasikan mapping ke 'Skor_Rating'
df_ulasan['Label_Sentimen'] = df_ulasan['Skor_Rating'].map(sop_mapping)

print("\n--- DATASET SETELAH DILAKUKAN PELABELAN (ANNOTATION) ---")
# Menampilkan seluruh kolom untuk melihat kecocokan teks, rating, dan hasil label
print(df_ulasan)