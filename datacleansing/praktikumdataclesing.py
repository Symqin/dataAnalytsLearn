import pandas as pd
import numpy as np


# PERSIAPAN DATASET PENJUALAN

# Membaca dataset
data = {
    'ID_Transaksi': ['TRX01', 'TRX02', 'TRX03', 'TRX04', 'TRX05', 'TRX06', 'TRX07', 'TRX08', 'TRX09', 'TRX10'],
    'Produk': ['Laptop', 'Ponsel', 'Tablet', 'Laptop', 'Ponsel', 'Ponsel', 'Tablet', 'Laptop', 'Ponsel', 'Tablet'],
    'Kategori': ['Elektronik', 'Elektronik', np.nan, 'Elektronik', 'Elektronik', 'Elektronik', np.nan, 'Elektronik', 'Elektronik', 'Elektronik'], # Terdapat nilai hilang (NaN)
    'Harga': [15000, 8000, 5000, np.nan, 8000, -8000, 5000, 15000, 8000, np.nan], # Terdapat nilai hilang dan data salah (minus)
    'Jumlah_Beli': [2, 1, 3, 5, 2, 1, np.nan, 100, 2, 4] # Terdapat nilai hilang dan outlier ekstrim (100)
}

df = pd.DataFrame(data)

# Tahap 1 DATA UNDERSTANDING
print("========Tahap 1: Data Understanding========")
print("Dataset Penjualan:")
print(df)

print("\nInformasi Dataset:")
print(df.info())

print("\nTipe Data:")
print(df.dtypes)

print("\njumlah Nilai Hilang:")
print(df.isnull().sum())

# Tahap 2 DATA CLEANING
print("========Tahap 2: Data Cleaning========")
# A. Pengisian Nilai Hilang

#katergori yang hilang diisi dengan modus
mode_kategori = df['Kategori'].mode()[0]
df['Kategori'] = df['Kategori'].fillna(mode_kategori)

# Harga yang hilang diisi dengan median
median_harga = df['Harga'].median()
df['Harga'] = df['Harga'].fillna(median_harga)

# Jumlah_Beli yang hilang diisi dengan mean
mean_jumlah_beli = df['Jumlah_Beli'].mean()
df['Jumlah_Beli'] = df['Jumlah_Beli'].fillna(mean_jumlah_beli)

print("\nDataset Setelah Data Cleaning:")
print(df.isnull().sum())

# B. Penanganan Data Salah
# hapus data yang memiliki harga negatif
df = df.drop(df[df['Harga'] < 0].index)

print("\nDataset Setelah Penanganan Data Salah:")
print(df)

# C. Penanganan Outlier
Q1 = df['Jumlah_Beli'].quantile(0.25)
Q3 = df['Jumlah_Beli'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# menampilkan batas wajar
print(f"\nBatas Bawah Jumlah_Beli: {lower_bound}")
print(f"Batas Atas Jumlah_Beli: {upper_bound}")

# melakukan clipping pada kolom Jumlah_Beli
df['Jumlah_Beli'] = df['Jumlah_Beli'].clip(lower_bound, upper_bound)

print("\nDataset Setelah Penanganan Outlier:")
print(df)

# Deskripsi statistik setelah data cleansing
print("\nDeskripsi Statistik Setelah Data Cleansing:")
print(df.describe())



